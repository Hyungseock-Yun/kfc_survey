from selenium import webdriver
import random

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome('/home/ubuntu/python/chromedriver', options=options)
# browser = webdriver.Chrome('C:\\WorkSpace\\chromedriver\\chromedriver.exe') -- 로컬용
browser.get('https://s.kfcvisit.com/kor')


def _next_button():
    browser.find_element_by_id('NextButton').click()
    browser.implicitly_wait(2)


def _find_button_and_click(xpath):
    button = browser.find_element_by_xpath(xpath)
    button.click()


def choice_random():
    radio = browser.find_elements_by_tag_name("label")
    random.choice(radio).click()


# 시리얼번호 입력
insert_serial_number = browser.find_element_by_id('InputCouponNum')
insert_serial_number.click()
insert_serial_number.send_keys('1410677130121200588')

# 다음 버튼 클릭
_next_button()

# 라디오를 감싸고있는 span, 또는 해당 선택지의 label을 클릭하는게 쉬움.

# 주문 유형 선택
_find_button_and_click("//*[@for='R001000.1']")

# 주문 방법 선택
_find_button_and_click("//*[@for='R002000.6']")

# 다음 버튼 클릭
_next_button()

# 전반적 만족도 #
_find_button_and_click("//*[@id='FNSR006000']/td[2]/span")

# 다음 버튼 클릭
_next_button()

# 부분별 만족도 #
# 서비스 속도
_find_button_and_click("//*[@id='FNSR013000']/td[2]")

# 음식의 맛
_find_button_and_click("//*[@id='FNSR007000']/td[2]")

# 직원의 친절함
_find_button_and_click("//*[@id='FNSR020000']/td[2]")

# 레스토랑의 청결함
_find_button_and_click("//*[@id='FNSR024000']/td[2]")

# 직원들 청결 및 위생
_find_button_and_click("//*[@id='FNSR000133']/td[2]")

# 주문 정확도
_find_button_and_click("//*[@id='FNSR009000']/td[2]")

# 전반적 가치
_find_button_and_click("//*[@id='FNSR032000']/td[2]")

# 다음 버튼 클릭
_next_button()

# 방문 시 문제 여부 #
_find_button_and_click("""//*[@id="FNSR033000"]/td[3]""")

# 다음 버튼 클릭
_next_button()

# 고객 경험 설문조사 작성 #
customer_experience = browser.find_element_by_xpath("""//*[@id="S081000"]""")
customer_experience.click()
customer_experience.send_keys('직원이 친절하고 음식이 매우 맛있음')

# 다음 버튼 클릭
_next_button()

# 추가 질문 여부 #
_find_button_and_click("""//*[@id="FNSR000094"]/td[2]""")

# 다음 버튼 클릭
_next_button()

# 음식의 맛에 가장 영향을 끼친 음식
choice_random()

# 다음 버튼 클릭
_next_button()

# 고객 다음 예상 행동 #
# 향후 30일 이내 재방문 여부
_find_button_and_click("""//*[@id="FNSR035000"]/td[2]""")

# 향후 30일 이내 추천 여부
_find_button_and_click("""//*[@id="FNSR036000"]/td[2]""")

# 다음 버튼 클릭
_next_button()

# 직원 칭찬 여부 #
_find_button_and_click("""//*[@id="FNSR038000"]/td[2]""")

# 다음 버튼 클릭
_next_button()

# 직원 칭찬
compliment_staff = browser.find_element_by_xpath("""//*[@id="S081001"]""")
compliment_staff.click()
compliment_staff.send_keys('박진우 직원을 칭찬합니다. 친절한 메뉴설명과 미소 덕분에 기분 좋게 먹고 갑니다.')

# 다음 버튼 클릭
_next_button()

# 방문 계기
choice_random()

# 다음 버튼 클릭
_next_button()

# 설문조사 고지 유무
_find_button_and_click("""//*[@id="FNSR003000"]/td[2]""")

# 다음 버튼 클릭
_next_button()

# 정기 구독 유무
_find_button_and_click("""//*[@id="FNSR048000"]/td[3]""")

# 다음 버튼 클릭
_next_button()

browser.close()
