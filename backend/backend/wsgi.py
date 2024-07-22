import os
import environ
from django.core.wsgi import get_wsgi_application


env = environ.Env()
environ.Env.read_env(os.path.join(os.path.dirname(__file__), "..", ".env"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")


application = get_wsgi_application()
