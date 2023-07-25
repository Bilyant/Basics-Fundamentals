from django.db import models


class KeyWord(models.Model):
    name = models.CharField(max_length=30)
