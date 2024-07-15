import os
from .base import *  # noqa: F403, F401

environment = env("DJANGO_ENV")

if environment == "prod":
    from .prod import *  # noqa: F403, F401
elif environment == "test":
    from .test import *  # noqa: F403, F401
else:
    from .dev import *  # noqa: F403, F401
