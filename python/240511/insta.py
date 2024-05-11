# 라이브러리 로드 
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
from dotenv import load_dotenv
import time

# 이미지를 저장하는 함수를 생성 
# 매개변수 3개 : 이미지의 주소, 저장되는 위치, 파일의 이름 
def image_save(img_path, save_path, file_name):
    html_data = requests.get(img_path)
    # 파일이 저장되는 경로와 파일의 이름은 지정
    imageFile = open(
        os.path.join(
            save_path, 
            file_name
        ), 
        'wb'
    )
    # 이미지 데이터의 크기 지정
    chunk_size = 100000000
    for chunk in html_data.iter_content(chunk_size):
        imageFile.write(chunk)
        imageFile.close()
    print(f'{file_name} 저장 완료')


# .env 파일을 적용 
load_dotenv()

# selenium 라이브러리 이용하여 Chrome 브라우져 실행
driver = webdriver.Chrome()

# 인스타그램에 접속 
driver.get("https://www.instagram.com")

# 페이지가 로드 될때까지 대기 
# case1 : selenium -> 페이지가 로드될때까지 대기(로드가 완료되면 바로 실행) -> ex) 10초 대기를 설정하고 3초만에 로드가 완료되면 바로 실행
driver.implicitly_wait(10)
# case2 : time -> 강제적으로 코드의 실행을 중지 -> ex) 10초 대기를 설정하면 10초를 대기하고 다음 코드 실행
time.sleep(1)
# 인스타그램 로그인하기 위해 id, password를 입력
# id를 입력하는 태그를 선택 
id_element = driver.find_element(
    By.CSS_SELECTOR, 
    'input[name="username"]'
)
# env에 있는 id를 id_element에 입력
id_element.send_keys(os.getenv('id'))

# password를 입력하는 태그를 선택 
pass_element = driver.find_element(
    By.CSS_SELECTOR, 
    'input[name="password"]'
)
# pass_element에 env에 있는 password를 입력
pass_element.send_keys(os.getenv('password'))
# pass_element에서 ENTER키 이벤트를 발생
pass_element.send_keys(Keys.ENTER)

driver.implicitly_wait(10)
time.sleep(1)
# 검색 아이콘 태그를 선택 
search_element = driver.find_element(
    By.CSS_SELECTOR, 
    'svg[aria-label="검색"]'
)
# 검색 아이콘을 클릭 이벤트를 발생
search_element.click()

driver.implicitly_wait(10)

# 검색어를 입력하는 태그를 선택 
search_input = driver.find_element(
    By.CSS_SELECTOR, 
    'input[aria-label="입력 검색"]'
)
# 검색어를 입력 
search_input.send_keys('강남역 맛집')

driver.implicitly_wait(10)
time.sleep(1)

# 검색 리스트가 포함되어있는 태그를 선택
# CSS_SELECTOR -> 
#   태그명[속성명=속성값]
#   class의 이름으로 검색 -> .class명
#   id의 값으로 검색 -> #id값
#   div 태그 안에 a 태그 -> div a
list_element = driver.find_elements(
    By.CSS_SELECTOR, 
    '.x9f619.x78zum5.xdt5ytf.x1iyjqo2.x6ikm8r.x1odjw0f.xh8yej3.xocp1fn a'
)
# list_element의 원소의 개수 
print(len(list_element))

# list_element에서 첫번째 a태그를 클릭
list_element[0].click()

driver.implicitly_wait(10)
time.sleep(1)

# 게시물 목록을 생성 
imgs = driver.find_elements(
    By.CLASS_NAME, 
    '_aagw'
)
# 게시물 중 첫번째 태그를 선택하여 클릭
imgs[0].click()

# data를 저장할 변수를 생성 
data = {
    'ID' : [], 
    'contents' : []
}
# 이미지의 주소들이 추가가 될 빈 리스트 생성
img_list = []
# 대기 시간
driver.implicitly_wait(10)
time.sleep(1)
# 몇개의 게시물에 데이터를 가져올것인가? 반복문을 이용하여 생성
# 반복 횟수(3회)
i = 0
end_val = 1
while True:
    # 게시물에 있는 데이터를 data변수에 대입 
    driver.implicitly_wait(10)
    time.sleep(1)
    ids = driver.find_elements(
        By.CLASS_NAME, 
        '_a9zc'
    )
    contents = driver.find_elements(
        By.CLASS_NAME, 
        '_a9zs'
    )
    # ids, contents 기준으로 반복문을 실행
    for id, content in zip(ids, contents):
        data['ID'].append(id.text)
        data['contents'].append(content.text.replace('\n', ' '))

    # 이미지 다음버튼이 존재할때 반복 실행(무한실행)
    while True:
        driver.implicitly_wait(10)
        # 이미지 태그를 모두 찾는다. 
        img_elements = driver.find_elements(
            By.CSS_SELECTOR, 
            '._aagu._aato ._aagv img'
        )
        for img_element in img_elements:
            # img_element에 src 속성의 값을 img_list에 추가 (img_list에 존재하지 않는 경우에만)
            src_data = img_element.get_attribute('src')
            if src_data not in img_list:
                img_list.append(src_data)
        try:
            # 이미지에서 다음버튼 클릭 
            img_next = driver.find_element(
                By.CSS_SELECTOR, 
                'button[aria-label="다음"]'
            )
            img_next.click()
        except:
            # 두번째 while문을 강제 종료
            break
    
    # 만약에 i이 end_val보다 같다면 -> 반복문을 종료
    if i == end_val:
        break
    # i의 값은 1씩 증가
    i += 1
    # 다음 버튼이 존재하지 않는다면 -> 반복문을 종료
    try:
        next_element = driver.find_element(
            By.CSS_SELECTOR, 
            'svg[aria-label="다음"]'
        )
        next_element.click()
    except:
        print('next error')
        break
# 게시물 닫기 
close_element = driver.find_element(
    By.CSS_SELECTOR, 
    'svg[aria-label="닫기"]'
)
close_element.click()
# 만들어진 data 출력
print(data)

# 현재 시간 
now = time.strftime('%y-%m-%d %H_%M_%S')
# 파일명에 ':' 사용 불가

# data라는 변수를 데이터프레임으로 생성 
df = pd.DataFrame(data)
# 데이터프레임을 csv로 저장 
df.to_excel(f"df{now}.xlsx")

file_num = 0
for img in img_list:
    image_save(img, "./imgs", f"img{now}_{file_num}.png")
    file_num += 1