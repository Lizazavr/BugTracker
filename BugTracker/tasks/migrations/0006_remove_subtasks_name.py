# Generated by Django 4.2.16 on 2024-09-14 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_subtasks_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtasks',
            name='name',
        ),
    ]
