from django.contrib import admin

from .models import Category, Book, Author

class AuthorAdmin(admin.ModelAdmin):

  filter_horizontal = ('books',)
  list_display = ['name', 'description']

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Author, AuthorAdmin)