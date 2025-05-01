from bs4 import BeautifulSoup
import requests

def parse():
    url = 'https://omgtu.ru/general_information/departments/publishers/staff/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    arr = soup.find_all('a', {'style': 'font-size: 180%;'})

    for el in arr:
        name = el.text
        if name[0].lower() == 'н':
            with open('lab1result.txt', 'a', encoding='utf8') as file:
                file.write(f'{name}\n')

if __name__ == '__main__':
    parse()












