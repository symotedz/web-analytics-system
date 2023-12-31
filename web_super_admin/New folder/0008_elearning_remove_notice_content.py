# Generated by Django 4.2.1 on 2023-09-05 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_super_admin', '0007_assignment_date_posted'),
    ]

    operations = [
        migrations.CreateModel(
            name='ELearning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('posted_by', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('link', models.SlugField()),
            ],
        ),
        migrations.RemoveField(
            model_name='notice',
            name='content',
        ),
    ]
