from django.apps import AppConfig

class EmpAppConfig(AppConfig):
    name = 'emp_app'

    def ready(self):
        import emp_app.signals
