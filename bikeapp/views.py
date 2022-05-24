import time
from django.shortcuts import render
from django.views.generic.base import TemplateView
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from django.views.decorators.csrf import csrf_exempt
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MainpageView(TemplateView):
    template_name = 'bikeapp/index.html'
# Create your views here.
def index(request):
    return render(request, 'index.html')

def findmap(request):
    return render(request, 'bikeapp/mapfind.html')

@csrf_exempt
def result(request):
    if request.method == 'POST':
        rt1 = request.POST['rt1']
        rt2 = request.POST['rt2']

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # driver = webdriver.Safari(executable_path='/usr/bin/safaridriver')
    driver = webdriver.Chrome('C:/Users/admin/Downloads/chromedriver.exe',options=options)
    

    driver.get('https://map.naver.com/v5/directions')
    driver.implicitly_wait(10)

    # 도보 선택
    driver.find_element(by=By.CSS_SELECTOR, value='ul[role=tablist] li:nth-child(3) > a').click()

    #### 출발지 입력
    driver.find_elements(by=By.CSS_SELECTOR, value='input.input_search')[0].send_keys(rt1)
    driver.find_elements(by=By.CSS_SELECTOR, value='input.input_search')[0].send_keys(Keys.RETURN)
    #<span _ngcontent-kwp-c100="" class="search_title_text">광명시립하안도서관</span>
    #driver.find_elements(by=By.CSS_SELECTOR, value='div.search_box')[0].click()


    time.sleep(0.3)
    #### 첫번째 장소 선택
    #driver.find_element(by=By.CSS_SELECTOR, value='ul.list_place:last-child li.item_place.ng-star-inserted').click()

    #driver.implicitly_wait(0.3)
    #### 도착지 입력
    driver.find_elements(by=By.CSS_SELECTOR, value='input.input_search')[1].send_keys(rt1+'따릉이')
    driver.find_elements(by=By.CSS_SELECTOR, value='input.input_search')[1].send_keys(Keys.RETURN)

    time.sleep(0.5)
    #### 첫번째 장소 선택
    #driver.find_element(by=By.CSS_SELECTOR, value='ul.list_place:last-child li.item_place.ng-star-inserted').click()

    time.sleep(0.3)
    ## 길찾기 선택
    driver.find_elements(by=By.CSS_SELECTOR, value='div.btn_box > button')[2].click()

    time.sleep(0.5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    table1 = soup.select('span.value.ng-star-inserted')
    hm = soup.select('span.unit.ng-star-inserted')

    if hm[0].text == '시간':
        print(table1[0].text,'시간',table1[1].text,"분")
        starttobike = int(table1[0].text) * 60 + int(table1[1].text)
    elif hm[0].text  == '분':
        print(table1[0].text,'분')
        starttobike = int(table1[0].text)
    else:
        print('검색결과가 없습니다.')
    

    #data = {'sb':starttobike}

    #자전거 선택
    driver.find_element(by=By.CSS_SELECTOR, value='ul[role=tablist] li:last-child > a').click()

    #### 출발지 입력
    driver.find_elements(by=By.CSS_SELECTOR, value='input.input_search')[0].clear()
    driver.find_elements(by=By.CSS_SELECTOR, value='input.input_search')[0].send_keys(rt1+'따릉이')
    driver.find_elements(by=By.CSS_SELECTOR, value='input.input_search')[0].send_keys(Keys.RETURN)

    time.sleep(0.5)
    #### 첫번째 장소 선택
    #driver.find_element(by = By.CSS_SELECTOR, value='ul.list_place li.item_place').click()

    time.sleep(0.2)
    #### 도착지 입력
    driver.find_elements(by=By.CSS_SELECTOR, value='input.input_search')[1].clear()
    driver.find_elements(by=By.CSS_SELECTOR, value='input.input_search')[1].send_keys(rt2+'따릉이')
    driver.find_elements(by=By.CSS_SELECTOR, value='input.input_search')[1].send_keys(Keys.RETURN)

    time.sleep(0.3)
    #### 첫번째 장소 선택
    # driver.find_element(by = By.CSS_SELECTOR, value='ul.list_place li.item_place').click()
    ## 길찾기 선택
    driver.find_elements(by=By.CSS_SELECTOR, value='div.btn_box > button')[2].click()


    time.sleep(0.3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    
    #table2 = soup.select('.item_summary.selected.ng-star-inserted span.value.ng-star-inserted')
    # print(len(table2))
    #item_summary selected ng-star-inserted

    
    #print(table2[0].text,'분')
    table2 = soup.select('span.value.ng-star-inserted')
    hm = soup.select('span.unit.ng-star-inserted')
    print(hm[0].text)

    if hm[0].text == '시간':
        print(table2[0].text,'시간',table2[1].text,"분")
        bikeroute = int(table2[0].text) * 60 + int(table2[1].text)
    elif hm[0].text == '분':
        print(table2[0].text,'분')
        bikeroute = int(table2[0].text)
    else:
        print('검색결과가 없습니다.')

# item_summary ng-star-inserted 
# item_summary selected ng-star-inserted

    # 도보 선택
    driver.find_element(by=By.CSS_SELECTOR, value='ul[role=tablist] li:nth-child(3) > a').click()

    #### 출발지 입력
    driver.find_elements(by=By.CSS_SELECTOR, value='input.input_search')[0].clear()
    driver.find_elements(by=By.CSS_SELECTOR, value='input.input_search')[0].send_keys( rt2+'따릉이')
    driver.find_elements(by=By.CSS_SELECTOR, value='input.input_search')[0].send_keys(Keys.RETURN)

    time.sleep(1)
    #### 첫번째 장소 선택
    #driver.find_element(by=By.CSS_SELECTOR, value='ul.list_place li.item_place').click()

    time.sleep(0.5)
    #### 도착지 입력
    driver.find_elements(by=By.CSS_SELECTOR, value='input.input_search')[1].clear()
    driver.find_elements(by=By.CSS_SELECTOR, value='input.input_search')[1].send_keys(rt2)
    driver.find_elements(by=By.CSS_SELECTOR, value='input.input_search')[1].send_keys(Keys.RETURN)

    time.sleep(0.3)
    #### 첫번째 장소 선택
    # driver.find_element(by=By.CSS_SELECTOR, value='ul.list_place li.item_place').click()
    ## 길찾기 선택
    driver.find_elements(by=By.CSS_SELECTOR, value='div.btn_box > button')[2].click()


    time.sleep(0.5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    table3 = soup.select('span.value.ng-star-inserted')
    print(table3)
    print(table3[0].text,'분')

    biketodest = int(table3[0].text)
    total = starttobike + bikeroute + biketodest 

    data = {'sb':starttobike, 'br':bikeroute,'bd': biketodest, 'total' : total}
    return render(request, 'bikeapp/result.html', data)

def directions(request):
    return render(request, 'bikeapp/directions.html')