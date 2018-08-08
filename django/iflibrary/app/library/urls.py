from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [

    # Books
    path('books/', views.BooksView.as_view(), name='book-list'),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/<pk>/', views.BookView.as_view(), name='book-detail'),
    path('books/<pk>/update/', views.BookUpdateView.as_view(), name='book-update'),

    # Categories
    path('categories/', views.CategoriesView.as_view(), name='category-list'),
    path('categories/<pk>', views.CategoryView.as_view(), name='category-detail'),

    # Categories
    path('reservation/create/', views.ReservationCreateView.as_view(), name='reservation-create'),

]
