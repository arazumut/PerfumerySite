# Perfume Cosmetic Website

Perfume Cosmetic is a Django-based e-commerce website designed to sell cosmetic products. With its user-friendly interface and modern design, it is an ideal platform for online sales of cosmetic products.

## Features

- Responsive design for proper display on all devices
- Product categories and subcategories
- Detailed product pages
- Wishlist and cart features
- User account management
- Payment integration
- Easy content management with admin panel
- Blog system
- Contact form

## Screenshots
 <img width="1710" alt="Screen Shot 2025-04-28 12 23 36" src="https://github.com/user-attachments/assets/f5b92035-0451-47df-8a90-61efbb91951a" /> 


## Technologies

- **Backend**: Django 4.2+
- **Frontend**: HTML5, CSS3, JavaScript, UIKit
- **Database**: SQLite (Development), PostgreSQL (Recommended for Production)
- **CSS Frameworks**: UIKit
- **Icon Library**: Font Awesome 5
- **Others**: jQuery, Swiper.js

## Installation

### Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)
- Git

### Steps

1. Clone the project:
```bash
git clone https://github.com/username/CosmeticWebSite.git
cd CosmeticWebSite/Cosmetic
```

2. Create and activate a virtual environment:
```bash
# Linux/macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create and migrate the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create an admin user:
```bash
python manage.py createsuperuser
```

6. Collect static files:
```bash
python manage.py collectstatic
```

7. Start the server:
```bash
python manage.py runserver
```

8. Visit the following URL in your browser:
```
http://127.0.0.1:8000/
```

## Usage

### Admin Panel

To access the admin panel, visit `http://127.0.0.1:8000/admin/` and log in with your superuser credentials. Through this panel, you can:

- Add/edit/delete categories and products
- Manage blog posts
- View users and orders
- Change site settings

### Product Management

1. Go to the "ParfumeCosmetic" section in the admin panel
2. Click on "Categories" or "Products"
3. Use the "Add" button to add new items
4. Click on existing items to edit them

## Deployment to Production

Follow these steps to run the project in a production environment:

1. Change the `DEBUG` setting to `False` in `settings.py`
2. Set a secure value for `SECRET_KEY` (use environment variables)
3. Update the `ALLOWED_HOSTS` setting
4. Consider switching to a more powerful database like PostgreSQL or MySQL
5. Use Nginx or Apache to serve static files
6. Install an SSL certificate for HTTPS

## Structure

Project structure:

- `ParfumeCosmetic/`: Main application directory
  - `models.py`: Database models
  - `views.py`: View functions
  - `urls.py`: URL routers
  - `admin.py`: Admin panel registrations
  - `templates/`: HTML templates
  - `static/`: Static files (CSS, JS, images)
- `myproject/`: Project configuration directory
  - `settings.py`: Project settings
  - `urls.py`: Main URL routers
- `media/`: User-uploaded files
- `static/`: Collected static files
- `manage.py`: Django management script
- `requirements.txt`: Required Python packages

## Contributing

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to your branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

