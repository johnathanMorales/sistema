# Generated by Django 3.2.8 on 2021-12-02 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_auto_20211202_0541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='descricion',
            new_name='descripcion',
        ),
    ]
