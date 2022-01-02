from bs4 import BeautifulSoup
import requests
from application.models import Teachers
from application.models import Groups


def getSoup(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    return soup


def createTeachers():
    url = 'https://pnu.edu.ru/rasp/teacher'

    soup = getSoup(url).find_all('div', class_='page-content')
    soup = soup[0].find_all('li')


    for i in soup:
        href = 'https://pnu.edu.ru/rasp/teacher/{}'.format(i.find_all('a', href=True)[0]['href'])

        s = i.text.split()
        if len(s) < 3:
            # в случае если в s будет только содержаться два списка добавляет третий список
            s.append(' ')
        Teachers.objects.create(first_name=s[0], last_name=s[1], midle_name=s[2], rtgKnow=0, rtgTeaching_skill=0,
                                rtgCommunication=0, rtgFreebie=0, rtgOverall_score=0, link=href)


def getGroups():
    #Добавляет группы в бд Teachers
    #!работает долго
    print('starter...')
    teaLink = Teachers.objects.in_bulk()
    for i in teaLink:
        listGroup = []

        url = teaLink[i].link
        soup = getSoup(url).find_all('td', class_='time-group')

        for q in range(len(soup)):
            listGroup.append(''.join(soup[q].text.split()))


        for w in set(listGroup):
            Groups.objects.create(first_name=teaLink[i].first_name, last_name=teaLink[i].last_name, midle_name=teaLink[i].midle_name, group=w.upper())
            #tea = Teachers.objects.get(first_name=teaLink[i].first_name, last_name=teaLink[i].last_name, midle_name=teaLink[i].midle_name)
            #tea.Groups.add(dj_object)


def parsingTeacher(text):
    if isinstance(text, list) == False:
        text = text.split()

    d = {'Должность': 'post', 'Образование': 'teachingLevel', 'Квалификации': 'teachingQual',
         'Научно-педагогический стаж': 'specExperience'}
    infoList = []
    a = Teachers.objects.filter(first_name=text[0], last_name=text[1], midle_name=text[2])

    html = requests.get(a[0].link)
    soup = BeautifulSoup(html.text, 'lxml')
    soup = soup.find_all('table')
    for j, i in d.items():
        s = soup[0].find_all(attrs={'itemprop': i})
        infoList.append('\n' + j + ':' + ' '.join(s[0].text.split()))

    return ' '.join(infoList)
