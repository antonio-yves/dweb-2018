from django.db import models

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