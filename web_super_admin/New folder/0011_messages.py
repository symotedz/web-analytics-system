# Generated by Django 4.2.1 on 2023-09-15 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_super_admin', '0010_rename_class_block_class_create_school_block_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_combinations', models.CharField(max_length=255)),
                ('school', models.CharField(max_length=255)),
                ('status', models.BooleanField()),
                ('date_posted', models.DateTimeField(max_length=255)),
                ('posted_by', models.CharField(max_length=255)),
            ],
        ),
    ]
