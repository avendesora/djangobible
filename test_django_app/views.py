from django.shortcuts import render


def verse_tag_views(request):
    data = {
        "verse_id": 1001001,
        "version": "ASV",
        "full_title": True,
    }

    return render(request, "verse_tags.html", data)
