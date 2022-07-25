from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'image', 'description']
    list_display = ('title', 'image', 'creation_date', 'creator')
    list_filter = ['creation_date', 'creator']
    search_fields = ['title']

admin.site.register(Book, BookAdmin)