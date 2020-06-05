from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json, requests
options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(executable_path='geckodriver', options=options)


def get_image(username):
    global driver
    driver.get('https://www.instadp.com/fullsize/{}'.format(username))
    img = driver.find_element_by_class_name('picture').get_attribute('src')

    if len(img) != 0:
        return img
    else:
        req = json.loads(requests.get('https://www.instagram.com/{}/?__a=1'.format(username)).text)
        if len(req) > 0:
            return req['graphql']['user']['profile_pic_url_hd']
        else:
            return -1

