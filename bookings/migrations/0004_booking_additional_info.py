# Generated by Django 4.2.13 on 2024-06-11 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='additional_info',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
