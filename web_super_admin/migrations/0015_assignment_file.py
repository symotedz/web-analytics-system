# Generated by Django 4.2.7 on 2023-12-21 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_super_admin', '0014_alter_staff_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
