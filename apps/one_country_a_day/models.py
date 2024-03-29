from django.db import models


class Country(models.Model):
    alpha_2 = models.CharField(max_length=2, blank=False)
    alpha_3 = models.CharField(max_length=3, blank=False)
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class CountryData(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    history = models.TextField()
    flag = models.TextField()
    cuisine = models.TextField()
    dish = models.TextField()
    area = models.TextField()
    population = models.TextField()
    fauna = models.TextField()
    food_production = models.TextField()
    borders = models.TextField()
