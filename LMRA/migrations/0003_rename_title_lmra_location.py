# Generated by Django 4.2 on 2023-05-05 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LMRA', '0002_lmra_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lmra',
            old_name='title',
            new_name='location',
        ),
    ]
