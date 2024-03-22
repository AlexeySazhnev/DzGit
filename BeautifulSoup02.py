from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getAtriboot(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        # Выводит все указанные теги
        nameList = bsObj.findAll('span', {'class': 'green'})
        # nameList =bs0bj.find('span', {'class':'green'}) # Выводит первый указанный тег
    except AttributeError as e:
        return None
    return nameList


myList = getAtriboot('http://bit.ly/1Ge96Rw')
if myList == None:
    print('Не удалось найти!')
else:
    for name in myList:
        print(name.get_text())

# html = urlopen('http://bit.ly/1Ge96Rw')
# bs0bj = BeautifulSoup(html.read())
# nameList =bs0bj.findAll(text='the prince') -- Найти колличество конкретного слова внутри тега
# print(len(nameList))
