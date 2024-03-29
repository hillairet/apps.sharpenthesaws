from datetime import timedelta
from pathlib import Path

from django.utils import timezone


def retrieve_tomorrows_countrys_data() -> None:
    from .models import CountryData

    tmpfile = Path('/tmp/djangotest')

    try:
        latest_entry = CountryData.objects.latest('created_at')
    except CountryData.DoesNotExist:
        next_country = _retrieve_next_countrys_data()
        tmpfile.write_text('Called _retrieve_next_countrys_data in exception')
        return

    now = timezone.now()

    time_since_last_country_data = now - latest_entry.created_at

    if time_since_last_country_data < timedelta(days=1):
        return

    next_country = _retrieve_next_countrys_data()

    tmpfile.write_text('Called _retrieve_next_countrys_data')


def _retrieve_next_countrys_data() -> int:
    return 3
