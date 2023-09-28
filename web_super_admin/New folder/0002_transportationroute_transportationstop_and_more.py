# Generated by Django 4.2.1 on 2023-09-03 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_super_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransportationRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TransportationStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TransportationStopOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_super_admin.transportationroute')),
                ('stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_super_admin.transportationstop')),
            ],
        ),
        migrations.AddField(
            model_name='transportationroute',
            name='stops',
            field=models.ManyToManyField(through='web_super_admin.TransportationStopOrder', to='web_super_admin.transportationstop'),
        ),
        migrations.CreateModel(
            name='TransportationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_requested', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected')], max_length=1)),
                ('approved_at', models.DateTimeField(blank=True, null=True)),
                ('rejected_at', models.DateTimeField(blank=True, null=True)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_super_admin.transportationroute')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_super_admin.student')),
            ],
        ),
    ]