# 🛒 GreatKart – Django E-commerce Web Application

GreatKart is a Django-based E-commerce web application developed as part of my academic learning and practical implementation of full-stack web development using Django.  

This project demonstrates authentication, custom user forms, product management, cart functionality, and structured project architecture following Django’s MVT pattern.

---

## 🚀 Project Overview

GreatKart is designed to simulate a basic online shopping platform where users can:

- Register and create an account
- Login and Logout securely
- Browse products by category
- View product details
- Add products to cart
- Manage cart items
- Admin manage products and categories

The project follows industry-standard Git workflow and version control practices using Git & GitHub.

---

## 🧩 Features Implemented

### 🔐 Authentication Module (accounts app)
- User Registration
- Login / Logout
- Custom User Forms
- Form Validation
- Form Overriding & Customization
- Django Built-in Authentication System

### 🏬 Store Module (store app)
- Product Listing Page
- Product Detail Page
- Dynamic Product Display
- Category Filtering

### 🗂 Category Module (category app)
- Product Categories
- Category-wise Product Display

### 🛒 Cart Module (carts app)
- Add to Cart Functionality
- Remove from Cart
- Quantity Management
- Session-based Cart Handling

### ⚙ Admin Customization
- Custom Admin Panel Configuration
- Product & Category Management
- User Management

---

## 🏗 Project Architecture

This project follows Django’s **MVT (Model-View-Template)** architecture:

- **Model** → Database structure using Django ORM  
- **View** → Business logic and request handling  
- **Template** → Frontend UI rendering  

---

## 🛠 Technologies Used

| Layer | Technology |
|-------|------------|
| Backend | Python, Django |
| Frontend | HTML, CSS, Bootstrap |
| Database | SQLite |
| Version Control | Git & GitHub |
| IDE | VS Code |

---

## 📂 Project Structure

```
GreatKart/
│
├── accounts/        # Authentication & user management
├── carts/           # Cart functionality
├── category/        # Product categories
├── store/           # Product management
├── templates/       # HTML templates
├── static/          # CSS, JS, Images
├── greatkart/       # Project settings
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup Guide

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/girishnshobha1524-wq/greatkart-django.git
cd greatkart-django
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv env
```

Activate environment:

Windows:
```bash
env\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 5️⃣ Run Development Server

```bash
python manage.py runserver
```

Open browser:
```
http://127.0.0.1:8000/
```

---

## 🔐 Admin Access

Create superuser:

```bash
python manage.py createsuperuser
```

Access admin panel at:

```
http://127.0.0.1:8000/admin/
```

---

## 🎯 Learning Outcomes

Through this project, I learned:

- Django project structure and app architecture
- Custom user model & authentication flow
- Form overriding and validation
- Django ORM and database migrations
- Git version control and GitHub repository management
- Structured code organization and modular development

---

## 📌 Future Enhancements

- Payment Gateway Integration
- Order Management System
- Email Verification
- User Profile Dashboard
- Product Search & Filtering
- Deployment on Cloud (AWS / Heroku)

---

## 👨‍💻 Author

**Girish N**  
GitHub: https://github.com/girishnshobha1524-wq  
Email: girishnshobha1524@gmail.com

---

## 📄 License

This project is developed for educational purposes.

    