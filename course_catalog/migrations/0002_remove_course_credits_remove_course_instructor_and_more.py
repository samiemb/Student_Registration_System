# Generated by Django 5.1.2 on 2024-10-20 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='credits',
        ),
        migrations.RemoveField(
            model_name='course',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='course',
            name='title',
        ),
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
