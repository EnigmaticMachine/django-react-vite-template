import os

from django.core.wsgi import get_wsgi_application

environment = os.getenv("DJANGO_ENV", "dev")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

application = get_wsgi_application()
