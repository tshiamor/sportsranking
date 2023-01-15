from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Leaguerank(models.Model):
    name = models.CharField(max_length=200,)
    points = models.PositiveIntegerField(blank=True, null=True)
    ranking = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        if self.ranking:
            return f"{self.name} ({self.ranking})"
        return self.name

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))

                if field.verbose_name != 'team'

                else
                    (field.verbose_name,
                    Team.objects.get(pk=field.value_from_object(self)).name)






                for field in self.__class__._meta.fields[1:]
            ]
