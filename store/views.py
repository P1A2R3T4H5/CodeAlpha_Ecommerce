from decimal import Decimal
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .models import Product, Order, OrderItem
from .forms import RegisterForm, CheckoutForm

def home(request):
    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()
    products = Product.objects.all()
    if query:
        products = products.filter(name__icontains=query) | products.filter(description__icontains=query)
    if category:
        products = products.filter(category__iexact=category)
    categories = Product.objects.values_list("category", flat=True).distinct().order_by("category")
    return render(request, "store/home.html", {"products": products.distinct(), "categories": categories, "query": query, "selected_category": category})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "store/product_detail.html", {"product": product})

def _cart_items(request):
    cart = request.session.get("cart", {})
    items, total = [], Decimal("0.00")
    for product_id, qty in cart.items():
        try:
            product = Product.objects.get(pk=int(product_id))
            quantity = max(1, int(qty))
            quantity = min(quantity, product.stock)
            if quantity:
                line_total = product.price * quantity
                items.append({"product": product, "quantity": quantity, "line_total": line_total})
                total += line_total
        except (Product.DoesNotExist, ValueError, TypeError):
            continue
    return items, total

def cart_view(request):
    items, total = _cart_items(request)
    return render(request, "store/cart.html", {"items": items, "total": total})

@require_POST
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.stock < 1:
        messages.error(request, "This product is currently out of stock.")
        return redirect("product_detail", pk=pk)
    cart = request.session.get("cart", {})
    key = str(product.pk)
    cart[key] = min(int(cart.get(key, 0)) + int(request.POST.get("quantity", 1)), product.stock)
    request.session["cart"] = cart
    messages.success(request, f"{product.name} added to your cart.")
    return redirect(request.POST.get("next") or "cart")

@require_POST
def update_cart(request, pk):
    cart = request.session.get("cart", {})
    key = str(pk)
    if key in cart:
        try:
            quantity = int(request.POST.get("quantity", 1))
            product = Product.objects.get(pk=pk)
            if quantity <= 0:
                cart.pop(key, None)
            else:
                cart[key] = min(quantity, product.stock)
        except (ValueError, Product.DoesNotExist):
            cart.pop(key, None)
    request.session["cart"] = cart
    return redirect("cart")

@require_POST
def remove_from_cart(request, pk):
    cart = request.session.get("cart", {})
    cart.pop(str(pk), None)
    request.session["cart"] = cart
    messages.info(request, "Item removed from cart.")
    return redirect("cart")

@login_required
def checkout(request):
    items, total = _cart_items(request)
    if not items:
        messages.info(request, "Your cart is empty. Add a product before checkout.")
        return redirect("home")
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                # Re-check inventory during checkout to avoid overselling.
                for item in items:
                    product = Product.objects.select_for_update().get(pk=item["product"].pk)
                    if product.stock < item["quantity"]:
                        messages.error(request, f"Not enough stock for {product.name}. Please update your cart.")
                        return redirect("cart")
                order = Order.objects.create(
                    user=request.user,
                    full_name=form.cleaned_data["full_name"],
                    email=form.cleaned_data["email"],
                    phone=form.cleaned_data["phone"],
                    address=form.cleaned_data["address"],
                    city=form.cleaned_data["city"],
                    postal_code=form.cleaned_data["postal_code"],
                    total=total,
                )
                for item in items:
                    product = Product.objects.select_for_update().get(pk=item["product"].pk)
                    OrderItem.objects.create(order=order, product=product, product_name=product.name,
                                             unit_price=product.price, quantity=item["quantity"])
                    product.stock -= item["quantity"]
                    product.save(update_fields=["stock"])
            request.session["cart"] = {}
            return render(request, "store/order_success.html", {"order": order})
    else:
        initial = {"full_name": request.user.get_full_name(), "email": request.user.email}
        form = CheckoutForm(initial=initial)
    return render(request, "store/checkout.html", {"form": form, "items": items, "total": total})

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).prefetch_related("items")
    return render(request, "store/my_orders.html", {"orders": orders})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Your account has been created.")
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "store/register.html", {"form": form})
