# Generated by Django 3.2.7 on 2021-12-15 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_auto_20211207_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='data',
            field=models.DateField(auto_now_add=True, verbose_name='Дата'),
        ),
    ]