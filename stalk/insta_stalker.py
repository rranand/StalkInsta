import requests
from bs4 import BeautifulSoup
import re


def get_image(username):
    try:
        req = requests.get('https://www.instadp.com/fullsize/{}'.format(username))
    except requests.exceptions.ConnectionError:
        return -1

    soup = BeautifulSoup(req.text, 'html.parser')
    x = soup.prettify()
    link = re.findall('preloadImg\(\'(.+)\'\)', str(x))

    if len(link) == 1:
        return link[0]
    else:
        return -1
