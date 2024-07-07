from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('infrastructure/', include('infrastructure.urls')),

]
