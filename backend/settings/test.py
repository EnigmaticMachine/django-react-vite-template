from .base import BASE_DIR
from .base import LOGGING as BASE_LOGGING

DEBUG = True
ALLOWED_HOSTS = []

# Dadabase configuration for tests
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "ATOMIC_REQUESTS": True,
    }
}

LOGGING = BASE_LOGGING.copy()
LOGGING["loggers"]["django"]["level"] = "DEBUG"
LOGGING["loggers"]["core"]["level"] = "DEBUG"
LOGGING["handlers"]["console"]["formatter"] = "standard"
