from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.utils.request import Request

from bs4 import BeautifulSoup
import requests

from application.models import Teachers
#from proTgRating.application.models import Teachers


class Command(BaseCommand):
    help = 'Парсит сайт, затем добавляет преподователей в бд'

    def handle(self, *args, **options):

        html = requests.get('https://pnu.edu.ru/rasp/teacher')

        soup = BeautifulSoup(html.text, 'lxml')
        soup = soup.find_all('div', class_='page-content')
        soup = soup[0].find_all('li')

        for i in soup:
            s = i.text.split()
            if len(s) < 3:
                #в случае если в s будет только содержаться два списка добавляет третий список
                s.append(' ')
            Teachers.objects.create(first_name=s[0], last_name=s[1], midle_name=s[2], rtgKnow=0, rtgTeaching_skill=0,
                                    rtgCommunication=0, rtgFreebie=0, rtgOverall_score=0)


