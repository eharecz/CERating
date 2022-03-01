# Generated by Django 4.0.1 on 2022-02-19 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailcheck', '0004_alter_emailcheck_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('type', models.CharField(blank=True, max_length=32, null=True)),
                ('relation', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=32, null=True)),
                ('password', models.CharField(blank=True, max_length=64, null=True)),
                ('simulate_count', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'enterprise',
            },
        ),
        migrations.AlterModelTable(
            name='emailcheck',
            table='emailcheck',
        ),
    ]
