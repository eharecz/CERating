from django.db import models


# Create your models here.
class OfficialRatingGrade(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    industy_type = models.CharField(max_length=100, blank=True, null=True)
    classify = models.CharField(max_length=100, blank=True, null=True)
    grade = models.CharField(max_length=100, blank=True, null=True)
    word_frequency_score = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'Official_Rating_Grade'
