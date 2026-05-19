release: pip install setuptools wheel && python manage.py migrate --noinput
web: gunicorn mydjango.wsgi:application --log-file -