# Generated by Django 4.2.7 on 2023-12-22 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_super_admin', '0017_school_end_date_school_registration_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='super_admin_user',
            name='End_Date',
            field=models.DateField(blank=True, null=True),
        ),
    ]