from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'teambuilding.accounts'

    def ready(self):
        from . import receivers
