# Generated by Django 5.0.3 on 2024-03-28 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dzproj', '0010_remove_orders_warmage_ware_warmage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ware',
            old_name='warmage',
            new_name='image',
        ),
    ]