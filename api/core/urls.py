from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from core.settings import PREFIX_URL

urlpatterns = [
    path(PREFIX_URL+'admin/', admin.site.urls),
    path(PREFIX_URL+'', include('base.urls')),
]
