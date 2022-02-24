# KeitaBeauty-backend
Keita's Beauty is an online E-commerce Website where you can purchase your favorite make-up products for a reasonable price. Redux state management is used to handle cart functionality.

## App Screenshots

<img width="1395" alt="Screen Shot 2022-02-24 at 9 52 34 AM" src="https://user-images.githubusercontent.com/92543814/155548299-003fed6b-df9c-4b04-b25b-cfec1c46f430.png">


<img width="1293" alt="Screen Shot 2022-02-24 at 9 53 10 AM" src="https://user-images.githubusercontent.com/92543814/155548275-3c93e56b-c381-4be4-8881-bb8265933113.png">





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
```<img width="1037" alt="Screen Shot 2022-02-24 at 9 52 47 AM" src="https://user-images.githubusercontent.com/92543814/155548359-fcce2efe-7d0a-402d-9405-d930f6615be3.png">

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

## Major Hurdles
There were some issues during deployment and uploading static images with heroku. I tried using cloudinary media management services but decided to keep trying with whitenoise and everything worked out! 
