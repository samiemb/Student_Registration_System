# Generated by Django 5.1.2 on 2024-10-21 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_processing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(max_length=20),
        ),
    ]
