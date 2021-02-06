#!/usr/bin/python3
from selenium import webdriver

try:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome('/home/ubuntu/python/chromedriver', options=options)
    browser.get('http://www.google.com')
    browser.implicitly_wait(2)
    print("이상없이 실행됨")
    browser.implicitly_wait(2)
    browser.close()
except ModuleNotFoundError as e:
    print(e)
