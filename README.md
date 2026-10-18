# ShopNest — CodeAlpha E-commerce Internship Task

A responsive Django e-commerce demo built with HTML, CSS, JavaScript, Django, and SQLite.

## Features
- Responsive product catalogue with search and category filters
- Product detail pages
- Session-based shopping cart (add, update quantity, remove)
- Registration, login, and logout using Django authentication
- Authenticated checkout and order creation
- Order history for the signed-in user
- Stock validation and inventory reduction during order placement
- Django admin to manage products and orders
- Seed command with demo products
- CSRF protection and server-side form validation

## Tech stack
- Frontend: HTML5, CSS3, vanilla JavaScript
- Backend: Python + Django
- Database: SQLite (included with Django; database file is created locally)
- Authentication: Django's built-in user authentication

## Run locally (Windows / VS Code)

### 1. Open the project folder
Extract the ZIP, then open the `codealpha_ecommerce` folder in VS Code.

### 2. Create and activate a virtual environment
In the VS Code terminal (PowerShell):

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

### 3. Install Django
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Create database tables
```powershell
python manage.py migrate
```

### 5. Add sample products
```powershell
python manage.py seed_products
```

### 6. Start the development server
```powershell
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Optional: Django admin
Create an administrator:
```powershell
python manage.py createsuperuser
```
Then visit `http://127.0.0.1:8000/admin/` to manage products and orders.

## Suggested demo flow
1. Browse products and search for an item.
2. Open a product detail page and add it to the cart.
3. Update quantity or remove an item from the cart.
4. Register an account.
5. Proceed to checkout and place an order (demo checkout; no payment gateway).
6. Open **My orders** to view the order.
7. If desired, use the Django admin to view and update products and order status.

## Important notes
- Checkout creates an order but does not charge a payment method. Do not present it as a live payment gateway.
- Product images are loaded from Unsplash URLs, so an internet connection is needed for those images. Replace image URLs in the Django admin if desired.
- This is a local internship-task demo. Before public deployment, set `DEBUG = False`, use a secure environment-based `SECRET_KEY`, configure production hosts, HTTPS, and a production database.
- Do not commit your local `db.sqlite3`, secrets, or virtual environment to GitHub.

## GitHub submission checklist
- [ ] Run the app and test the full shopping flow.
- [ ] Add screenshots to the README if requested by CodeAlpha.
- [ ] Push source code and README to your own GitHub repository.
- [ ] Include the deployed URL only if you have actually deployed and tested it.
