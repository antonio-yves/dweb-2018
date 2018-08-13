from django.apps import AppConfig


class LibraryConfig(AppConfig):
    name = 'app.library'

    def ready(self):
        from . import signals
