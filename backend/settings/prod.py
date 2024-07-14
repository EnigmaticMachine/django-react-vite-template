from .base import env
from .base import LOGGING as BASE_LOGGING


DATABASES = {
    "default": env.db(),
}

# Security settings (only as a fallback)
# Django’s security middleware as a fallback
# to ensure your application is secure even if Nginx configuration is not applied.
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True  # Redirect all HTTP traffic to HTTPS if not handled by Nginx


LOGGING = BASE_LOGGING.copy()
LOGGING["handlers"]["file"] = {
    "class": "logging.FileHandler",
    "filename": "django.log",
    "formatter": "standard",
}

LOGGING["loggers"]["django"]["handlers"].append("file")
LOGGING["loggers"]["core"]["handlers"].append("file")
LOGGING["loggers"]["django"]["level"] = "INFO"
LOGGING["loggers"]["core"]["level"] = "INFO"
