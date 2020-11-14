import requests
from bs4 import BeautifulSoup


class GetEnglishWords:
    url = 'https://kreekly.com/random/'

    eng_list = []
    rus_list = []
    def __init__(self):
        pass

    def parse(self):
        full_page = requests.get (self.url)

        soup = BeautifulSoup (full_page.content ,'html.parser')
        convert = soup.find_all ("div" ,{"class": "dict-word"})

        con_soup = BeautifulSoup (str (convert) ,'html.parser')
        con_eng = con_soup.find_all ('span' ,{'class': 'eng'})
        con_rus = con_soup.find_all ('span' ,{'class': 'rus'})

        for i in con_eng:
            for j in i:
                self.eng_list.append (j)

        for i in con_rus:
            for j in i:
                self.rus_list.append (j)

        return self.eng_list, self.rus_list





