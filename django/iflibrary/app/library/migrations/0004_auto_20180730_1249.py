# Generated by Django 2.0.7 on 2018-07-30 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20180730_1243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='categor',
            new_name='category',
        ),
    ]
