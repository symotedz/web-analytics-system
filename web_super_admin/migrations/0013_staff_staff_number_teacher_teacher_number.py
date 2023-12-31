# Generated by Django 4.2.7 on 2023-12-21 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_super_admin', '0012_cashout'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='Staff_Number',
            field=models.PositiveBigIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='Teacher_Number',
            field=models.PositiveBigIntegerField(blank=True, null=True, unique=True),
        ),
    ]
