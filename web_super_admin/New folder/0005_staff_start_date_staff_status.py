# Generated by Django 4.2.1 on 2023-09-03 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_super_admin', '0004_opportunities'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
