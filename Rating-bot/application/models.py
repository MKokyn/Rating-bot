from django.contrib.postgres.fields import ArrayField
from django.db import models

#https://bitbucket.org/vkasatkin/td/src/master/tga/ugc/models.py
#https://django.fun/tutorials/
#https://django.fun/tutorials/uskorennyj-kurs-django/
#https://www.youtube.com/watch?v=QaxLpuDWvZI&list=PLDyJYA6aTY1nZ9fSGcsK4wqeu-xaJksQQ&index=2
#https://github.com/ohld/django-telegram-bot/blob/main/tgbot/models.py

class Teachers(models.Model):
    first_name = models.CharField(verbose_name='Фамилия', max_length=200)
    last_name = models.CharField(verbose_name='Имя', max_length=200)
    midle_name = models.CharField(verbose_name='Отчество', max_length=200)

    rtgKnow = models.FloatField()
    rtgTeaching_skill = models.FloatField()
    rtgCommunication = models.FloatField()
    rtgFreebie = models.FloatField()
    rtgOverall_score = models.FloatField()

    link = models.CharField(default=' ', verbose_name='Link', max_length=200)


class Groups(models.Model):
    first_name = models.CharField(verbose_name='Фамилия', max_length=200, default=' ')
    last_name = models.CharField(verbose_name='Имя', max_length=200, default=' ')
    midle_name = models.CharField(verbose_name='Отчество', max_length=200, default=' ')

    group  = models.CharField(verbose_name='Группы', max_length=200)
    teacher = models.ManyToManyField(Teachers)


# class Know(models.Model):
#     first_name = models.CharField(verbose_name='Фамилия', max_length=200, default=' ')
#     last_name = models.CharField(verbose_name='Имя', max_length=200, default=' ')
#     midle_name = models.CharField(verbose_name='Отчество', max_length=200, default=' ')
#
#     quantity_one = models.PositiveSmallIntegerField(default=0)
#     quantity_two = models.PositiveSmallIntegerField(default=0)
#     quantity_three = models.PositiveSmallIntegerField(default=0)
#     quantity_four = models.PositiveSmallIntegerField(default=0)
#     quantity_five = models.PositiveSmallIntegerField(default=0)
#
#
# class Teaching_skill(models.Model):
#     first_name = models.CharField(verbose_name='Фамилия', max_length=200, default=' ')
#     last_name = models.CharField(verbose_name='Имя', max_length=200, default=' ')
#     midle_name = models.CharField(verbose_name='Отчество', max_length=200, default=' ')
#
#     quantity_one = models.PositiveSmallIntegerField(default=0)
#     quantity_two = models.PositiveSmallIntegerField(default=0)
#     quantity_three = models.PositiveSmallIntegerField(default=0)
#     quantity_four = models.PositiveSmallIntegerField(default=0)
#     quantity_five = models.PositiveSmallIntegerField(default=0)
#
# class Communication(models.Model):
#     first_name = models.CharField(verbose_name='Фамилия', max_length=200, default=' ')
#     last_name = models.CharField(verbose_name='Имя', max_length=200, default=' ')
#     midle_name = models.CharField(verbose_name='Отчество', max_length=200, default=' ')
#
#     quantity_one = models.PositiveSmallIntegerField(default=0)
#     quantity_two = models.PositiveSmallIntegerField(default=0)
#     quantity_three = models.PositiveSmallIntegerField(default=0)
#     quantity_four = models.PositiveSmallIntegerField(default=0)
#     quantity_five = models.PositiveSmallIntegerField(default=0)
#
# class Freebie(models.Model):
#     first_name = models.CharField(verbose_name='Фамилия', max_length=200, default=' ')
#     last_name = models.CharField(verbose_name='Имя', max_length=200, default=' ')
#     midle_name = models.CharField(verbose_name='Отчество', max_length=200, default=' ')
#
#     quantity_one = models.PositiveSmallIntegerField(default=0)
#     quantity_two = models.PositiveSmallIntegerField(default=0)
#     quantity_three = models.PositiveSmallIntegerField(default=0)
#     quantity_four = models.PositiveSmallIntegerField(default=0)
#     quantity_five = models.PositiveSmallIntegerField(default=0)
#
# class Overall_score(models.Model):
#     first_name = models.CharField(verbose_name='Фамилия', max_length=200, default=' ')
#     last_name = models.CharField(verbose_name='Имя', max_length=200, default=' ')
#     midle_name = models.CharField(verbose_name='Отчество', max_length=200, default=' ')
#
#     quantity_one = models.PositiveSmallIntegerField(default=0)
#     quantity_two = models.PositiveSmallIntegerField(default=0)
#     quantity_three = models.PositiveSmallIntegerField(default=0)
#     quantity_four = models.PositiveSmallIntegerField(default=0)
#     quantity_five = models.PositiveSmallIntegerField(default=0)

class Reviews(models.Model):
    first_name = models.CharField(verbose_name='Фамилия', max_length=200, default=' ')
    last_name = models.CharField(verbose_name='Имя', max_length=200, default=' ')
    midle_name = models.CharField(verbose_name='Отчество', max_length=200, default=' ')

    id_tg = models.IntegerField()
    #email = models.CharField(verbose_name='Почта', max_length=200)

    Know = models.PositiveSmallIntegerField(default=0)
    Teaching_skill = models.PositiveSmallIntegerField(default=0)
    Communication = models.PositiveSmallIntegerField(default=0)
    Freebie = models.PositiveSmallIntegerField(default=0)
    Overall_score = models.PositiveSmallIntegerField(default=0)
    #data = models.CharField(verbose_name='Дата', max_length=100, default=' ')
    data = models.DateField(verbose_name='Дата')


class Students(models.Model):
    email = models.CharField(verbose_name='Почта', max_length=200)
    id_tg = models.IntegerField()
    faculty = models.CharField(verbose_name='Факультет', max_length=10)
    group = models.CharField(verbose_name='Группа', max_length=10)
    code = models.IntegerField()
    reg_status = models.BooleanField(default=False)
