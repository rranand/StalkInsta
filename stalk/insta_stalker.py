from selenium import webdriver
from selenium.webdriver.firefox.options import Options

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
        return -1
