# Generated by Django 3.1.6 on 2021-11-01 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Queries',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=30)),
                ('message', models.TextField(max_length=5000)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
