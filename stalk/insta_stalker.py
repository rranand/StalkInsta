import json
import requests
from bs4 import BeautifulSoup
import re

'''
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from django.conf import settings

options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(executable_path=settings.DRIVER_PATH, options=options)


def get_image(username):
    global driver
    driver.get('https://www.instadp.com/fullsize/{}'.format(username))
    img = driver.find_element_by_class_name('picture').get_attribute('src')

    if len(img) != 0:
        return img
    else:
        return get_image_json(username)
'''


def get_image(username):
    req = json.loads(requests.get('https://www.instagram.com/{}/?__a=1'.format(username)).text)
    if len(req) > 0:
        e = get_image_alter(username)

        if e != -1:
            return str(e)
        return str(req['graphql']['user']['profile_pic_url_hd'])
    else:
        return -1
    

def get_image_alter(username):
    try:
        r = requests.get('https://www.instadp.com/fullsize/{}'.format(username)).text
    except requests.exceptions.ConnectionError:
        return -1
    except requests.exceptions.Timeout:
        return -1
    except requests.exceptions.TooManyRedirects:
        return -1
    except requests.exceptions.RequestException:
        return -1
    soup = BeautifulSoup(r, features="html.parser")
    link = soup.select('img[class="picture"]')[0]['src']

    if len(link) > 0:
        return link
    return -1
