"""Views for functional testing djangobible."""

from __future__ import annotations

from django.shortcuts import render


def verse_tag_views(request):
    """View for testing verse tags."""
    view_data = {
        "verse_id": 1001001,
        "version": "KJV",
        "full_title": True,
    }

    return render(request, "verse_tags.html", view_data)
