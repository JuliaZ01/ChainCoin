# Generated by Django 2.1.7 on 2019-04-27 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermana', '0002_auto_20190427_2052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteer',
            old_name='Vl_detail',
            new_name='VL_Detail',
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='Vl_name',
            field=models.CharField(max_length=500),
        ),
    ]
