from .settings import *


# Dadabase configuration for tests
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "ATOMIC_REQUESTS": True,
    }
}


# # Override the database settings for testing
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'test_my_database',  # Use a specific test database name
#         'USER': 'my_user',
#         'PASSWORD': 'my_password',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# # You can also override other settings specific to testing
# # For example, use a faster password hasher
# PASSWORD_HASHERS = [
#     'django.contrib.auth.hashers.MD5PasswordHasher',
# ]

# # Disable migrations for faster test runs
# class DisableMigrations:
#     def __contains__(self, item):
#         return True

#     def __getitem__(self, item):
#         return "notmigrations"

# MIGRATION_MODULES = DisableMigrations()
