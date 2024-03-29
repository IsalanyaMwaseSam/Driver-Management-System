from django.apps import AppConfig


class DriverAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'driver_app'

    def ready(self):
        import driver_app.signals
