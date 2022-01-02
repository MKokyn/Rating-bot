from django.core.management.base import BaseCommand

from django.conf import settings
from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.ext import CallbackQueryHandler
from telegram.utils.request import Request
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


from application.models import Teachers
from application.models import Reviews
from application.models import Students
from application.models import Groups

import random
from datetime import date, datetime
from collections import Counter

from application.management.commands import email
from application.management.commands import parser


button1 = '0'
button2 = '1'
button3 = '2'
button4 = '3'
button5 = '4'
button6 = 'button6'
button7 = 'button7'

button8 = 'button8'
button9 = 'button9'
button10 = 'button10'
button11 = 'button11'
button12 = 'button12'

name_buttons = {
    button1:'Знания',
    button2:'Умение преподовтаь',
    button3:'Общение',
    button4:'Халявность',
    button5:'Общая оценка',
    button6:'<<',
    button7:'>>',

    button8:'1',
    button9:'2',
    button10:'3',
    button11:'4',
    button12:'5',
}

keyboard = [
    [
            InlineKeyboardButton(name_buttons[button8], callback_data=button8),
            InlineKeyboardButton(name_buttons[button9], callback_data=button9),
            InlineKeyboardButton(name_buttons[button10], callback_data=button10),
            InlineKeyboardButton(name_buttons[button11], callback_data=button11),
            InlineKeyboardButton(name_buttons[button12], callback_data=button12)
    ]
]

keyboard1 = [
    [
        InlineKeyboardButton(name_buttons[button1], callback_data=button1)
    ],
    [
        InlineKeyboardButton(name_buttons[button2], callback_data=button2)
    ],
    [
        InlineKeyboardButton(name_buttons[button3], callback_data=button3)
    ],
    [
        InlineKeyboardButton(name_buttons[button4], callback_data=button4)
    ],
    [
        InlineKeyboardButton(name_buttons[button5], callback_data=button5)
    ],

    [
        InlineKeyboardButton(name_buttons[button6], callback_data=button6),
        InlineKeyboardButton(name_buttons[button7], callback_data=button7)
    ]

    ]

def get_info(update, context):
    pass

counterInlKeyboard = [0]
keyS = {'0':'Know',#
        '1':'Teaching_skill',
        '2':'Communication',
        '3':'Freebie',
        '4':'Overall_score'}
conditionKeyboard = [0]#




def deleteTeachers(chatid, group):
    tea = [[i.first_name, i.last_name, i.midle_name] for i in Groups.objects.filter(group=group)]

    copytea = tea.copy()

    for i in range(len(copytea)):
        t = Reviews.objects.filter(first_name=copytea[i][0], last_name=copytea[i][1], midle_name=copytea[i][2], id_tg=chatid)
        #.exists()
        if t.count():
            if 0 not in (t[0].Know, t[0].Teaching_skill, t[0].Communication, t[0].Freebie, t[0].Overall_score):
                tea.pop(i)

    return tea


def eval_teachers(update, context):
    chat = update.effective_chat

    query = update.callback_query
    data = query.data

    group = Students.objects.filter(id_tg=chat.id)
    group = group[0].group

    tea = deleteTeachers(chat.id, group.upper())

    q=0


    if data == button7:
        if len(counterInlKeyboard) > 0:
            q = counterInlKeyboard[-1]

        q = q + 1

        #counterInlKeyboard.append(q)

        if q >= len(tea):
            q = len(tea)
        counterInlKeyboard[0] = q

        text = tea[q][0] + ' ' + tea[q][1] + ' ' + tea[q][2]
        print(text)
        reply_text = text + ' ' + str(q) + '/' + str(len(tea)) + '\n' + parser.parsingTeacher(text)

        query.edit_message_text(text=reply_text, reply_markup=InlineKeyboardMarkup(keyboard1))

    if data == button6:
        if len(counterInlKeyboard) > 0:
            q = counterInlKeyboard[-1]

        q = q - 1
        if q <= 0:
            q = 0
        counterInlKeyboard[0] = q
        #counterInlKeyboard.append(q)

        text = tea[q][0] + ' ' + tea[q][1] + ' ' + tea[q][2]
        reply_text = text + ' ' + str(q) + '/' + str(len(tea)) + '\n' + parser.parsingTeacher(text)

        query.edit_message_text(text=reply_text, reply_markup=InlineKeyboardMarkup(keyboard1))

    if data in (button1, button2, button3, button4, button5):
        conditionKeyboard[0] = data#
        print(keyboard1[0])
        #делаю копию что бы keyboard1 при обновление не сохранял keyboard
        keyboard1Copy = keyboard1.copy()
        keyboard1Copy[int(data)] = keyboard[0]
        text = tea[counterInlKeyboard[0]][0] +' '+ tea[counterInlKeyboard[0]][1]  +' '+ tea[counterInlKeyboard[0]][2]
        reply_text = text + ' '+ str(counterInlKeyboard[0]) + '/' + str(len(tea)) + '\n' + parser.parsingTeacher(text)

        query.edit_message_text(text=reply_text, reply_markup=InlineKeyboardMarkup(keyboard1Copy))

    if data in (button8, button9, button10, button11, button12):
        #print(keyS[conditionKeyboard[0]]+'  '+name_buttons[data])
        text = query['message']['text'].split('\n')[0].split(' ')
        print(int(name_buttons[data]))
        if conditionKeyboard[0] == button1:
            #date.today()
            values_for_update = {'first_name':text[0], 'last_name':text[1], 'midle_name':text[2], 'id_tg':chat.id, 'Know':int(name_buttons[data]), 'data':date.today()}
            Reviews.objects.update_or_create(first_name=text[0], last_name=text[1], midle_name=text[2], id_tg=chat.id, data=date.today(), defaults=values_for_update)
           #Reviews.objects.create(first_name=text[0], last_name=text[1], midle_name=text[2], id_tg=chat.id, Know=int(name_buttons[data]), data=date.today())
        if conditionKeyboard[0] == button2:
            values_for_update = {'first_name': text[0], 'last_name': text[1], 'midle_name': text[2], 'id_tg': chat.id,
                                 'Teaching_skill': int(name_buttons[data]), 'data': date.today()}
            Reviews.objects.update_or_create(first_name=text[0], last_name=text[1], midle_name=text[2], id_tg=chat.id,
                                             data=date.today(), defaults=values_for_update)
            #Reviews.objects.create(first_name=text[0], last_name=text[1], midle_name=text[2], id_tg=chat.id, Teaching_skill=int(name_buttons[data]), data=date.today())
        if conditionKeyboard[0] == button3:
            values_for_update = {'first_name': text[0], 'last_name': text[1], 'midle_name': text[2], 'id_tg': chat.id,
                                 'Communication': int(name_buttons[data]), 'data': date.today()}
            Reviews.objects.update_or_create(first_name=text[0], last_name=text[1], midle_name=text[2], id_tg=chat.id,
                                             data=date.today(), defaults=values_for_update)
            #Reviews.objects.create(first_name=text[0], last_name=text[1], midle_name=text[2], id_tg=chat.id, Communication=int(name_buttons[data]), data=date.today())
        if conditionKeyboard[0] == button4:
            values_for_update = {'first_name': text[0], 'last_name': text[1], 'midle_name': text[2], 'id_tg': chat.id,
                                 'Freebie': int(name_buttons[data]), 'data': date.today()}
            Reviews.objects.update_or_create(first_name=text[0], last_name=text[1], midle_name=text[2], id_tg=chat.id,
                                             data=date.today(), defaults=values_for_update)
            #Reviews.objects.create(first_name=text[0], last_name=text[1], midle_name=text[2], id_tg=chat.id, Freebie=int(name_buttons[data]), data=date.today())
        if conditionKeyboard[0] == button5:
            values_for_update = {'first_name': text[0], 'last_name': text[1], 'midle_name': text[2], 'id_tg': chat.id,
                                 'Overall_score': int(name_buttons[data]), 'data': date.today()}
            Reviews.objects.update_or_create(first_name=text[0], last_name=text[1], midle_name=text[2], id_tg=chat.id,
                                             data=date.today(), defaults=values_for_update)
            #Reviews.objects.create(first_name=text[0], last_name=text[1], midle_name=text[2], id_tg=chat.id, Overall_score=int(name_buttons[data]), data=date.today())


def key(update, context):
    chat = update.effective_chat
    text = update.message.text

    group = Students.objects.filter(id_tg=chat.id)
    group = group[0].group
    #tea = Groups.objects.filter(group=g)
    tea = deleteTeachers(chat.id, group)


    text = tea[0][0] +' '+ tea[0][1] +' '+ tea[0][2]
    reply_text = text + ' ' + str(0) + '/' + str(len(tea)) + '\n' + parser.parsingTeacher(text)

    context.bot.send_message(chat_id=chat.id, text=reply_text, reply_markup=InlineKeyboardMarkup(keyboard1))


def accept_group(update, context):
    chat = update.effective_chat
    text = update.message.text
    text = text.upper()
    Students.objects.filter(id_tg=chat.id).update(group=text)

    reply_text = '{Описание бота}'
    reply_keyboard = [['Оценка преподователей', 'Информация о боте']]

    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    context.bot.send_message(chat_id=chat.id, text=reply_text, reply_markup=markup)

def keyboard_handler(update, context):
    chat = update.effective_chat
    text = update.message.text


def get_teachers(update, context):
    chat = update.effective_chat
    text = update.message.text

    if len(text) > 5:
        text = text[1:].split(' ')

        info = Teachers.objects.filter(first_name=text[0],last_name=text[1],midle_name=text[2])

        reply_text = 'Описание преподователя'
        context.bot.send_message(chat_id=chat.id, text=reply_text)


def start(update: Update, context: CallbackContext):
    chat = update.effective_chat

    reply_text = "Для доступа к боту введите свою кооперативную почту. Пример: 20201234@pnu.edu.ru"
    context.bot.send_message(chat_id=chat.id, text=reply_text)

def accept_mail(update, context):
    chat = update.effective_chat
    text = update.message.text

    code = ''.join([random.choice(list('1234567890')) for x in range(4)])
    Students.objects.create(email=text, id_tg=chat.id, faculty='', group='', code=code, reg_status=False)
    email.send_mail(text, code)

    reply_text = 'Мы отправли код для авторизации на почту.'
    context.bot.send_message(chat_id=chat.id, text=reply_text)


def check_code(update, context):
    chat = update.effective_chat
    text = update.message.text
    if text.isspace():
        text = text.replace(' ', '')

    if text == str(Students.objects.get(id_tg=chat.id).code):
        Students.objects.filter(id_tg=chat.id).update(reg_status=True)

        #reply_text = 'Укажите свой факультет.'
        reply_text = 'Укажите свою группу. Пример: лх(б)-01'
        #context.bot.send_message(chat_id=chat.id, text=reply_text, reply_markup=get_keyboard())
        context.bot.send_message(chat_id=chat.id, text=reply_text)

    else:
        reply_text = 'Неверно указали код.'
        context.bot.send_message(chat_id=chat.id, text=reply_text)

def rating_calculation(text):
    inf = Reviews.objects.filter(first_name=text[0], last_name=text[1], midle_name=text[2])
    # inf[0].__dict__[q] for q in ['Know']
    if len(inf) != 0:
        s = Counter([inf[i].Know for i in range(len(inf))])
        rtgKnow = round(sum([i * s[i] for i in s.keys()]) / sum([s[i] for i in s.keys()]), 1)

        s = Counter([inf[i].Teaching_skill for i in range(len(inf))])
        rtgTeaching_skill = round(sum([i * s[i] for i in s.keys()]) / sum([s[i] for i in s.keys()]), 1)

        s = Counter([inf[i].Communication for i in range(len(inf))])
        rtgCommunication = round(sum([i * s[i] for i in s.keys()]) / sum([s[i] for i in s.keys()]), 1)

        s = Counter([inf[i].Freebie for i in range(len(inf))])
        rtgFreebie = round(sum([i * s[i] for i in s.keys()]) / sum([s[i] for i in s.keys()]), 1)

        s = Counter([inf[i].Overall_score for i in range(len(inf))])
        rtgOverall_score = round(sum([i * s[i] for i in s.keys()]) / sum([s[i] for i in s.keys()]), 1)


        reply_text = f'Знания {rtgKnow}\nУмение преподовать {rtgTeaching_skill}\nОбщение {rtgCommunication}\nХалявность {rtgFreebie}\nОбщая оценка {rtgOverall_score}'
    else:
        reply_text = f'Знания {0}\nУмение преподовать {0}\nОбщение {0}\nХалявность {0}\nОбщая оценка {0}'

    return reply_text




def find_teacher(update, context):
    chat = update.effective_chat
    text = update.message.text

    text += ' '
    text = text.split(' ')
    reply_text = ' '.join(text) + '\n' + parser.parsingTeacher(text) + '\nРейтинг:' + '\n' + rating_calculation(text)
    context.bot.send_message(chat_id=chat.id, text=reply_text)





class Command(BaseCommand):
    help = 'Telegram-bot'

    def __init__(self):
        if len(Teachers.objects.in_bulk()) <= 0:
            parser.createTeachers()


    def handle(self, *args, **options):
        request = Request(connect_timeout=0.5, read_timeout=1.0,)
        bot = Bot(request=request, token=settings.TOKEN_TELEGRAM_BOT)
        updater = Updater(bot=bot, use_context=True)

        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(MessageHandler(Filters.regex(r'@pnu.edu.ru'), accept_mail))
        dispatcher.add_handler(MessageHandler(Filters.regex(r'\d{4}'), check_code))
        dispatcher.add_handler(CallbackQueryHandler(callback=eval_teachers))
        #dispatcher.add_handler(CommandHandler('Информация о боте',get_info))
        #dispatcher.add_handler(CommandHandler('Оценка преподователей', key))
        dispatcher.add_handler(MessageHandler(Filters.regex('Оценка преподователей'), key))
        dispatcher.add_handler(MessageHandler(Filters.regex(r'^[й-ю]'), accept_group))
        dispatcher.add_handler(MessageHandler(Filters.regex(r'/'), get_teachers))
        dispatcher.add_handler(MessageHandler(Filters.regex(r'[А-ЯЁ][а-яё]+\s+[А-ЯЁ][а-яё]+(?:\s+[А-ЯЁ][а-яё]+)?'),find_teacher))



        updater.start_polling()
        updater.idle()
