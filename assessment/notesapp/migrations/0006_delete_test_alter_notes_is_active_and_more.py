# Generated by Django 4.2.21 on 2025-05-18 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0005_alter_users_create_on'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AlterField(
            model_name='notes',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
