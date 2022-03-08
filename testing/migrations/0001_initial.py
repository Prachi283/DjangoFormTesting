# Generated by Django 4.0.2 on 2022-03-08 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('position', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('phone_no', models.IntegerField()),
            ],
        ),
    ]
