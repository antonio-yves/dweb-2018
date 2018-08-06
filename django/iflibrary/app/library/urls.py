from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [

    # Books
    path('books/', views.BooksView.as_view(), name='book-list'),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/<pk>/', views.BookView.as_view(), name='book-detail'),

    # Categories
    path('categories/', views.CategoriesView.as_view(), name='category-list'),
    path('categories/<pk>', views.CategoryView.as_view(), name='category-detail'),

]
