from django.db import models

# Create your models here.
class level_result(models.Model):
    level = models.IntegerField(primary_key=True)