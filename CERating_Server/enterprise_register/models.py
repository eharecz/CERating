from django.db import models

# Create your models here.
class Emailcheck(models.Model):
    email = models.CharField(primary_key=True,max_length=32, blank=True)
    code = models.IntegerField(blank=True, null=True)
    timestamp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emailcheck'

class Enterprise(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    relation = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=32, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    simulate_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enterprise'