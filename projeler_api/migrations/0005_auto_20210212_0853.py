# Generated by Django 2.2 on 2021-02-12 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeler_api', '0004_auto_20210211_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='project',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='project',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='project',
            name='password',
        ),
        migrations.RemoveField(
            model_name='project',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='project',
            name='bolge',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='kod',
            field=models.CharField(max_length=4),
        ),
    ]