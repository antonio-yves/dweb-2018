from django.contrib import admin

from .models import Category, Book, Author, Reservation

class AuthorAdmin(admin.ModelAdmin):

  filter_horizontal = ('books',)
  list_display = ['name', 'description']

class BookAdmin(admin.ModelAdmin):

  list_display = ['name', 'total', 'available']

admin.site.register(Category)
admin.site.register(Book, BookAdmin)
admin.site.register(Reservation)
admin.site.register(Author, AuthorAdmin)