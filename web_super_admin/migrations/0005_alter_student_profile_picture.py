# Generated by Django 4.2.1 on 2023-09-23 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_super_admin', '0004_exam_block_exam_class_name_exam_time_alter_exam_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_picture',
            field=models.FileField(max_length=200, upload_to=''),
        ),
    ]
