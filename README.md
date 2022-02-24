# KeitaBeauty-backend
Keita's Beauty is an online E-commerce Website where you can purchase your favorite make-up products for a reasonable price. Redux state management is used to handle cart functionality.
	
## Getting Started

Create a project:
```
pip install django
pip install djangorestframework
django-admin startproject projectname .
./manage.py migrate
./manage.py createsuperuser
```
Add following to your settings.py module:
```
INSTALLED_APPS = [
    ...  # Make sure to include the default installed apps here.
    'rest_framework',
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}
```

To start a new server, run this command:
```
./manage.py runserver
```
## Technologies Used

- Django RestFramework
- Python
- Djoser
- Whitenoise
- Heroku
