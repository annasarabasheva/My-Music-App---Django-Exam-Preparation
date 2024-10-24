# Generated by Django 4.2.16 on 2024-10-24 09:49

import django.core.validators
from django.db import migrations, models
import profiles.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), profiles.validators.validate_username])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(blank=True, null=True, validators=[profiles.validators.validate_age])),
            ],
        ),
    ]
