from datetime import datetime

from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from django.urls import reverse_lazy

from . import models, forms

# Book list view
# - - - - - - - - - - - - - - - - - - -
class BooksView(ListView):

    model = models.Book
    template_name = 'book/list.html'

    def get_context_data(self, **kwargs):
        kwargs['categories'] = models.Category.objects.all()

        return super(BooksView, self).get_context_data(**kwargs)
    
    def get_queryset(self):
        if 'category' in self.request.GET:
            return models.Book.objects.filter(category=self.request.GET['category'])
        return models.Book.objects.all()

# Book - detail
# - - - - - - - - - - - - - - - - - - -
class BookView(DetailView):

    model = models.Book
    template_name = 'book/detail.html'

# Book - create
# - - - - - - - - - - - - - - - - - - -
class BookCreateView(CreateView):

    model = models.Book
    template_name = 'book/create.html'
    success_url = reverse_lazy('library:book-list')
    fields = ['name', 'description', 'isbn', 'year', 'edition', 'category']

# Book - update
# - - - - - - - - - - - - - - - - - - -
class BookUpdateView(UpdateView):

    model = models.Book
    template_name = 'book/create.html'
    success_url = reverse_lazy('library:book-list')
    fields = ['name', 'description', 'isbn', 'year', 'edition', 'category']

# Category list view
# - - - - - - - - - - - - - - - - - - -
class CategoriesView(ListView):

    model = models.Category
    template_name = 'category/list.html'

# Category detail
# - - - - - - - - - - - - - - - - - - -
class CategoryView(DetailView):

    model = models.Category
    template_name = 'category/detail.html'


# Reservation - create
# - - - - - - - - - - - - - - - - - - -
class ReservationCreateView(CreateView):

    model = models.Reservation
    template_name = 'reservation/create.html'
    success_url = reverse_lazy('library:book-list')
    form_class = forms.ReservationForm
    # fields = ['book', 'user']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.created_date = datetime.now()
        obj.updated_date = datetime.now()
        obj.save()        
        return super(ReservationCreateView, self).form_valid(form)