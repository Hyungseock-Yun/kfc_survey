from selenium import webdriver
import os


def auto_survey_start(number):
    print(number)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome('/home/ubuntu/python/chromedriver', options=options)
    # browser = webdriver.Chrome('C:\\WorkSpace\\chromedriver\\chromedriver.exe') -- 로컬용
    browser.get('https://s.kfcvisit.com/kor')
    attribute = browser.find_element_by_id("NextButton").get_attribute("value")
    type = browser.find_element_by_id("NextButton").get_attribute("type")
    name = browser.find_element_by_id("NextButton").get_attribute("name")
    print("attribute: " + attribute + ", type: " + type + ", name: " + name)

    browser.implicitly_wait(5)
    browser.close()

    pid = browser.service.process.pid
    print(pid)
    os.system("kill -15 {}".format(pid))
    print("taskKill success")