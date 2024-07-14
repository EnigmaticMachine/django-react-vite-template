from .base import env
from .base import LOGGING as BASE_LOGGING

DEBUG = env.bool("DEBUG", default=True)
LOGGING = BASE_LOGGING.copy()

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])

DATABASES = {
    "default": env.db(),
}

LOGGING["loggers"]["django"]["level"] = "DEBUG"
LOGGING["loggers"]["core"]["level"] = "DEBUG"
