from django.contrib import admin

from test_django_app.models import TestObject, TestSingleVerseObject

admin.site.register(TestObject)
admin.site.register(TestSingleVerseObject)
