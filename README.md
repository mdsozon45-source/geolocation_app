geolocation_app

Python 3.9.12
Django==4.2.7

python manage.py makemigrations geolocation
python manage.py migrate

template url "http://127.0.0.1:8000/location-data/"

api url "http://127.0.0.1:8000/api/location/"