# Generated by Django 5.1.1 on 2024-10-06 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_todolist_todolist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='todolist',
            new_name='user',
        ),
    ]
