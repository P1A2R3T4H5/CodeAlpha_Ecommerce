from django.core.management.base import BaseCommand
from store.models import Product

PRODUCTS = [
    ("Wireless Headphones", "Electronics", "Comfortable wireless headphones with clear sound and all-day battery life.", "2499.00", "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=900&q=85", 25, True),
    ("Everyday Sneakers", "Fashion", "Lightweight everyday sneakers designed for comfort, walking, and casual outfits.", "1899.00", "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=900&q=85", 18, True),
    ("Minimal Wrist Watch", "Accessories", "A clean, minimalist watch that works equally well for casual and formal occasions.", "3299.00", "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=900&q=85", 12, True),
    ("Travel Backpack", "Accessories", "A practical backpack with organized storage for commuting, college, and short trips.", "1499.00", "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&w=900&q=85", 30, False),
    ("Smartphone", "Electronics", "A modern smartphone for everyday communication, photography, and entertainment.", "15999.00", "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=900&q=85", 10, False),
    ("Ceramic Coffee Mug", "Home", "A durable ceramic mug for your coffee, tea, or favourite warm drink.", "399.00", "https://images.unsplash.com/photo-1514228742587-6b1558fcca3d?auto=format&fit=crop&w=900&q=85", 40, False),
    ("Desk Lamp", "Home", "A modern desk lamp for a focused workspace, reading corner, or study desk.", "999.00", "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?auto=format&fit=crop&w=900&q=85", 16, False),
    ("Classic Sunglasses", "Fashion", "Versatile sunglasses with a timeless silhouette for everyday outdoor wear.", "799.00", "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=900&q=85", 22, False),
]

class Command(BaseCommand):
    help = "Create demo products for the CodeAlpha shop."

    def handle(self, *args, **options):
        created = 0
        for name, category, description, price, image_url, stock, featured in PRODUCTS:
            _, was_created = Product.objects.get_or_create(
                name=name,
                defaults={"category": category, "description": description, "price": price,
                          "image_url": image_url, "stock": stock, "featured": featured},
            )
            created += int(was_created)
        self.stdout.write(self.style.SUCCESS(f"Seed complete. Added {created} new products."))
