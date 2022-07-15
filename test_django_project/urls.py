from __future__ import annotations

from django.contrib import admin
from django.urls import path

from test_django_app.views import verse_tag_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("verse_tags/", verse_tag_views),
]
