# Generated by Django 4.0.2 on 2022-02-17 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_remove_user_recipe_recipe_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]
