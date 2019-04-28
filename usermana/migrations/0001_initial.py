# Generated by Django 2.1.7 on 2019-04-27 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0004_users_bool'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blacklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bl_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vl_Detail', models.CharField(max_length=1000)),
                ('Vl_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Users')),
            ],
        ),
    ]
