# Generated by Django 4.2 on 2023-05-01 19:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0002_rename_subjects_taught_teacher_subjects_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="name",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="name",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="subjects",
            field=models.CharField(max_length=200),
        ),
    ]
