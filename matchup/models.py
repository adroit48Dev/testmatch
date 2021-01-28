
from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models





class GameList(models.Model):
    keyword = ArrayField(models.CharField(max_length=100))
    img_key = ArrayField(models.FileField(blank=True))
    definition = ArrayField(models.CharField(max_length=500))
    mat_name = models.CharField(max_length=100)

    def __str__(self):
        return self.mat_name
