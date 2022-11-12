from django.apps import AppConfig


class TransactionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'transactions'
    setup = False

    def ready(self):
        if self.setup:
            return

        from . import receivers

        self.setup = True
