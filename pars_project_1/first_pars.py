import requests
from bs4 import BeautifulSoup

url = 'https://primorye.ldpr.ru/'

def save_file_as_txt(file):
    with open(f'{file["title"]}.txt','w') as text:
        for txt in file:
            text.write(str(file[txt]))

def status_web_site(res):
    status = res.status_code
    if status == 200:
        return True
    return print(f'Status_code:{status}')

def get_news(url):
    res = requests.get(url)
    if status_web_site(res):
        soup = BeautifulSoup(res.text, "html.parser").find_all('a')
        lst_result = dict()
        for link in soup:
            if 'event' in str(link):
                news_soup = BeautifulSoup(requests.get(url + link.get('href')).text, "html.parser")
                lst_result['content'] = news_soup.find_all('p')
                lst_result['data'] = news_soup.find('div', class_='text-lg-right article-date').contents[0].strip()
                lst_result['title'] = news_soup.find('div', class_='e-title').contents[0].strip()
                save_file_as_txt(file=lst_result)

if __name__ == '__main__':
    get_news(url)