# Generated by Django 3.2.12 on 2023-06-23 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='introduction',
            field=models.TextField(default='Introduction', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(default='Nickname', max_length=40),
        ),
    ]