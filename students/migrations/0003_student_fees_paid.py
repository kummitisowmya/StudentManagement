# Generated by Django 4.2.14 on 2025-02-26 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_course_studentcourse_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='fees_paid',
            field=models.BooleanField(default=False),
        ),
    ]
