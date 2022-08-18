"""saas public URL Configuration
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # API endpoints
    path("api/", include([
        path("book/", include("apps.books.urls")),
    ])),
]
