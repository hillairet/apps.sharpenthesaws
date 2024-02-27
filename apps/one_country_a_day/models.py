from django.db import models


class Country(models.Model):
    alpha_2 = models.CharField(max_length=2, blank=False)
    alpha_3 = models.CharField(max_length=3, blank=False)
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name
