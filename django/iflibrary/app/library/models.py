from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):

  name = models.CharField(max_length=150, verbose_name='nome')
  description = models.TextField(verbose_name='descrição')

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'categoria de livro'
    verbose_name_plural = 'categorias de livro'


class Book(models.Model):

  name = models.CharField(max_length=150, verbose_name='nome')
  description = models.TextField(verbose_name='descrição')
  isbn = models.CharField(max_length=150, verbose_name='isbn')
  year = models.IntegerField()
  edition = models.IntegerField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books', verbose_name='categoria')
  total = models.IntegerField(default=1)
  available = models.IntegerField(default=1)

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'livro'
    verbose_name_plural = 'livros'


class Author(models.Model):

  name = models.CharField(max_length=150, verbose_name='nome')
  description = models.TextField(verbose_name='descrição')
  books = models.ManyToManyField(Book, related_name='authors', verbose_name='livros')

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'autor'
    verbose_name_plural = 'autores'


class Reservation(models.Model):

  STATUS = (
    (0, 'disponível'),
    (1, 'reservado'),
    (2, 'em falta')
  )

  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations', verbose_name='usuário')
  book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reservations', verbose_name='livro')
  status = models.IntegerField(choices=STATUS)
  created_date = models.DateTimeField(verbose_name='data empréstimo')
  updated_date = models.DateTimeField(verbose_name='data devolução')

  def __str__(self):
    return "%s - %s" % (self.book.name, self.user.username)
  
  class Meta:
    verbose_name = 'reserva'
    verbose_name_plural = 'reservas'