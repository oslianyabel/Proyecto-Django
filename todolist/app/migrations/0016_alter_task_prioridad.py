# Generated by Django 4.2.11 on 2024-04-06 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_task_vence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='prioridad',
            field=models.CharField(choices=[('baja', 'Baja'), ('media', 'Media'), ('alta', 'Alta')], max_length=10),
        ),
    ]