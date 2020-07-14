# Generated by Django 2.2 on 2020-07-14 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_event_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('location', models.CharField(max_length=100)),
                ('dateOuvertes', models.CharField(max_length=100)),
                ('heureOuvertes', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
