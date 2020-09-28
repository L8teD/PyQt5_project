import requests
from bs4 import BeautifulSoup

url = 'https://kreekly.com/random/'
headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',}

class get_english_words:
    url = 'https://kreekly.com/random/'
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36' ,}
    eng_list = []
    rus_list = []
    def __init__(self):
        pass

    def parse(self):
        full_page = requests.get (self.url ,headers=self.headers)

        soup = BeautifulSoup (full_page.content ,'html.parser')
        convert = soup.find_all ("div" ,{"class": "dict-word"})
        # print(str(convert))

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





#
#
#     f = open('translate.txt','a')
#     for i in range(len(eng_list)):
#         f.write("{}\t\t\t\t\t\t{}\n".format(eng_list[i],rus_list[i]))
#
# eng,rus = parse(url,headers)
#
# write_in_file(eng,rus)
# f = open('text.html','w',encoding='utf-8')
# f.write(full_page.text)





