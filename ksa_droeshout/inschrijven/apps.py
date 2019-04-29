from django.apps import AppConfig


class InschrijvenConfig(AppConfig):
    name = 'inschrijven'

    def ready(self):
        import inschrijven.signals
