# Generated by Django 2.2.1 on 2019-06-14 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raffle_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raffleentry',
            name='shoe_size',
            field=models.CharField(max_length=30),
        ),
    ]
