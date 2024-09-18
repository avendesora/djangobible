"""Views for functional testing djangobible."""

from __future__ import annotations

from typing import TYPE_CHECKING

from django.shortcuts import render

if TYPE_CHECKING:
    from django.http import HttpRequest
    from django.http import HttpResponse


def verse_tag_views(request: HttpRequest) -> HttpResponse:
    """View for testing verse tags."""
    view_data = {
        "verse_id": 1001001,
        "version": "KJV",
        "full_title": True,
    }

    return render(request, "verse_tags.html", view_data)
