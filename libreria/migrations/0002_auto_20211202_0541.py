# Generated by Django 3.2.8 on 2021-12-02 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='description',
        ),
        migrations.AddField(
            model_name='libro',
            name='descricion',
            field=models.TextField(null=True, verbose_name='Descripción'),
        ),
    ]