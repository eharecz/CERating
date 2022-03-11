from django.db import models

# Create your models here.
class Enterprise(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    relation = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=32, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    simulate_count = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enterprise'

class OfficialRatingGrade(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    industy_type = models.CharField(max_length=100, blank=True, null=True)
    classify = models.CharField(max_length=100, blank=True, null=True)
    grade = models.CharField(max_length=100, blank=True, null=True)
    word_frequency_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Official_Rating_Grade'

class EnterpriseData(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    co2_emission = models.FloatField(blank=True, null=True)
    environmental_protection_input = models.FloatField(blank=True, null=True)
    energy_onsumption = models.FloatField(blank=True, null=True)
    wastewater_discharge = models.FloatField(blank=True, null=True)
    waste_discharge = models.FloatField(db_column='Waste_discharge', blank=True, null=True)  # Field name made lowercase.
    cod_discharge = models.FloatField(db_column='COD_discharge', blank=True, null=True)  # Field name made lowercase.
    revenuein2020 = models.FloatField(db_column='RevenueIn2020', blank=True, null=True)  # Field name made lowercase.
    r_d_input = models.FloatField(db_column='R&D_input', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    industry_type = models.CharField(db_column='Industry_type', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'enterprise_data'

class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    owner_id = models.IntegerField(blank=True, null=True)
    goods_id = models.IntegerField(blank=True, null=True)
    order_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order'