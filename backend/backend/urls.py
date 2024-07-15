# from django.urls import path, include
# from django.contrib import admin
# from drf_spectacular.views import (
#     SpectacularAPIView,
#     SpectacularSwaggerView,
#     SpectacularRedocView,
# )

# from .views import error_count, health_check


# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("api/error-count/", error_count, name="error-count"),
#     path("api/health/", health_check, name="health_check"),

#     path("", include("core.urls")),
#     path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
#     path(
#         "api/docs/",
#         SpectacularSwaggerView.as_view(url_name="schema"),
#         name="swagger-ui",
#     ),
#     path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
# ]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("core.urls", namespace="core")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
