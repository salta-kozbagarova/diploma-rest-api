# Generated by Django 2.0.1 on 2018-01-19 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]