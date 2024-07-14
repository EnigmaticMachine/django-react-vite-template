from .base import *


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
