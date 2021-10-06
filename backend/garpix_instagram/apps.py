from django.apps import AppConfig


class GarpixInstagramConfig(AppConfig):
    name = 'garpix_instagram'
    verbose_name = 'Garpix Instagram'

    def ready(self):
        import property.signals  # noqa
