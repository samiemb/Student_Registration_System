# Generated by Django 5.1.2 on 2024-10-20 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_catalog', '0003_alter_course_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]