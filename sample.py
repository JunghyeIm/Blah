import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pyautogui
from selenium.webdriver.common.by import By
import time

#keyword = pyautogui.prompt("제품명을 입력하세요 : ")
keyword = "넘버즈인 클렌징오일"
searchUrl = f"https://www.oliveyoung.co.kr/store/search/getSearchMain.do?query={keyword}"

#-------------------------Selenium을 이용한 제어-------------------------#
#브라우저 생성
browser = webdriver.Chrome('') #/User/junghye/Documents/chromedriver
#웹사이트 열기
browser.get(searchUrl)
browser.implicitly_wait(10) #로딩이 끝날 때까지 10초 기다림
browser.find_element(By.CSS_SELECTOR,'.prd_info').click()
browser.find_element(By.CSS_SELECTOR,'#buyInfo').click()


infos = browser.find_elements(By.CSS_SELECTOR,'#artcInfo > dl.detail_info_list > dt')

cnt = 0
for i in infos :
    cnt += 1
    if i.text == "화장품법에 따라 기재해야 하는 모든 성분" : 
        print(cnt,  " : ", i.text)
        ingredientCnt = cnt
    else :
        print(cnt)


ingredient = browser.find_element(By.CSS_SELECTOR, f'#artcInfo > dl.detail_info_list:nth-child({ingredientCnt + 1}) > dd')
print("ingredient : ", ingredient.text)

ingredientList = ingredient.text.replace(" " , "").split(',')
for i in ingredientList :
    print("ingredient : ", i)


#-------------------------BeautifulSoup으로 html 분석-------------------------#

# header = {'User-agent' : 'Mozila/2.0'} #Connection aborted 봇 거절 에러 처리
# url = f"https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000166675&t_page=%ED%86%B5%ED%95%A9%EA%B2%80%EC%83%89%EA%B2%B0%EA%B3%BC%ED%8E%98%EC%9D%B4%EC%A7%80&t_click=%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_search_name={keyword}&t_number=1&dispCatNo=1000001000100080001&trackingCd=Result_1"
# response = requests.get(url, headers=header)
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')

# buyInfo = soup.select_one('#buyInfo')
# # buyInfo.attrs['class'] = "on"
# print(buyInfo)

# titles = soup.select('#artcInfo > dl.detail_info_list > dt') ##artcInfo > dl:nth-child(2) > dt
# print("titles : ", titles)
# for title in titles :
#     if title.text == "화장품법에 따라 기재해야 하는 모든 성분" : 
#         print(title.text)
#     else :
#         print("X : ", title.text)

