# Generated by Django 5.0.3 on 2024-03-07 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParkingFinderApp', '0002_parkingspace_delete_parkingspot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingspace',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
