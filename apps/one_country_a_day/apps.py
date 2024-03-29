from threading import Timer

from django.apps import AppConfig

from .tasks import retrieve_tomorrows_countrys_data


class OneCountryADayConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "one_country_a_day"

    def ready(self):
        thread = Timer(2, retrieve_tomorrows_countrys_data)
        thread.daemon = True
        thread.start()
