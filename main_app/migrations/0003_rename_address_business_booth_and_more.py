# Generated by Django 4.0.6 on 2022-07-12 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_business_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='address',
            new_name='booth',
        ),
        migrations.RenameField(
            model_name='business',
            old_name='city',
            new_name='social',
        ),
        migrations.RemoveField(
            model_name='business',
            name='state',
        ),
    ]
