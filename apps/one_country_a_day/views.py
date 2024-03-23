from django.shortcuts import render

from .models import Country


def index(request):
    context = {'countries': Country.objects.all()}
    return render(request, template_name="one-country-a-day/index.html", context=context)
