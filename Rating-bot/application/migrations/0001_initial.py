# Generated by Django 3.2.7 on 2021-09-26 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('last_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('midle_name', models.CharField(max_length=200, verbose_name='Отчество')),
                ('email', models.CharField(max_length=200, verbose_name='Почта')),
                ('Know', models.PositiveSmallIntegerField()),
                ('Teaching_skill', models.PositiveSmallIntegerField()),
                ('Communication', models.PositiveSmallIntegerField()),
                ('Freebie', models.PositiveSmallIntegerField()),
                ('Overall_score', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200, verbose_name='Почта')),
                ('id_tg', models.IntegerField()),
                ('faculty', models.CharField(max_length=10, verbose_name='Факультет')),
                ('group', models.CharField(max_length=10, verbose_name='Группа')),
                ('code', models.IntegerField()),
                ('reg_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('last_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('midle_name', models.CharField(max_length=200, verbose_name='Отчество')),
                ('rtgKnow', models.FloatField()),
                ('rtgTeaching_skill', models.FloatField()),
                ('rtgCommunication', models.FloatField()),
                ('rtgFreebie', models.FloatField()),
                ('rtgOverall_score', models.FloatField()),
            ],
        ),
    ]