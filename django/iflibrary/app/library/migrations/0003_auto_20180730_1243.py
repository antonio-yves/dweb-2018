# Generated by Django 2.0.7 on 2018-07-30 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20180730_1243'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'livro', 'verbose_name_plural': 'livros'},
        ),
    ]
