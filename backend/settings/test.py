from pathlib import Path
from .base import *


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
