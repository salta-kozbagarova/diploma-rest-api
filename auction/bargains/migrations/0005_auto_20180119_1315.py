# Generated by Django 2.0.1 on 2018-01-19 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bargains', '0004_auto_20180118_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bargain',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bargaintype',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]