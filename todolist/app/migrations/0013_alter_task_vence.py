# Generated by Django 3.2.24 on 2024-03-21 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_task_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='vence',
            field=models.DateField(null=True),
        ),
    ]
