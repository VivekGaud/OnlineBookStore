from django.contrib import admin
from books.models import book_details,book_category


admin.site.register(book_category)
admin.site.register(book_details)