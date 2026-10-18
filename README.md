# ShopNest — E-Commerce Website

ShopNest is a Django-based e-commerce web application developed as part of the CodeAlpha internship task.

The application provides a simple shopping experience where users can browse products, view product details, register or log in, manage their cart, and place orders.

## Features

- Product listing and browsing
- Individual product detail pages
- User registration and login
- User logout
- Shopping cart
- Checkout and order placement
- Order confirmation
- User order history
- Database-backed product and order management
- Responsive interface using HTML, CSS, and JavaScript

## Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Django

### Database
- SQLite for local development

### Version Control
- Git
- GitHub

## Project Structure

```text
CodeAlpha_Ecommerce/
├── manage.py
├── requirements.txt
├── README.md
├── shopsite/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── store/
│   ├── migrations/
│   ├── management/
│   │   └── commands/
│   │       └── seed_products.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
├── templates/
│   └── store/
└── static/
    └── store/
        ├── app.js
        └── styles.css
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/P1A2R3T4H5/CodeAlpha_Ecommerce.git
cd CodeAlpha_Ecommerce
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Apply database migrations

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

Open the following address in your browser:

http://127.0.0.1:8000/

## Database

The application uses SQLite for local development.

The local database file is excluded from version control. Running the migrations creates a new database, and the sample-product command populates it with sample products.

## Security Notes

- Do not commit passwords, private API keys, or production secrets.
- Use environment variables for sensitive settings in production.
- Configure Django's production security settings before deployment.
- Do not use Django's development server as a production web server.

## Future Improvements

- Payment gateway integration
- Product search and filtering
- Product ratings and reviews
- Order status tracking
- Product image management
- Production database integration

## Repository

GitHub: https://github.com/P1A2R3T4H5/CodeAlpha_Ecommerce

## Project Purpose

This project demonstrates fundamental e-commerce functionality using Django, Python, HTML, CSS, and JavaScript.