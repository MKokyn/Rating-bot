# Generated by Django 3.2.7 on 2021-12-15 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_alter_reviews_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='email',
        ),
    ]
