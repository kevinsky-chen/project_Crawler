from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys      #啟動捲動網頁等一些特殊鍵

driverPath = "C:\Program Files (x86)\chromedriver\chromedriver.exe"   # !!!一定要有driver
browser = webdriver.Chrome(driverPath)
url = 'https://www.google.com.tw'
browser.get(url)

"""
以下是王者selenium解析網頁元素的方法:(if沒找到,會產生NoSuchElement異常)
"""
select = browser.find_element_by_css_selector("input[title=搜尋][type=text]")    #找填表單.搜尋列處
select.send_keys(input())      #填寫表單.搜尋列(以"append"操作)
select.submit()          #填寫完成,送出表單

urlList = browser.find_elements_by_css_selector("cite[class=iUh30]")
urlListFin = []
for i in range(len(urlList)):
    urlListFin.append(urlList[i].text)
print(urlListFin)
try:
    selectFirst = browser.find_element_by_css_selector("h3.r a")      #用串列傳回所有符合CSS selector的元素
    title = selectFirst.text
    eleLink = browser.find_element_by_link_text(title)
    time.sleep(1)  # 暫停1秒
    eleLink.click()

    """
    for i in range(1,len(urlListFin)):
        # 第2~n個 tab  失敗:待修正!!!!!
        #browser.execute_script(str(window.open('about:blank', 'tab'+str(i+1))))
        #browser.switch_to_window("tab"+str(i+1))
        #browser.get(urlListFin[i])
        window_after = browser.window_handles[i]
        browser.switch_to_window(window_after)
        time.sleep(1)
        browser.get(urlListFin[i])
        """
except Exception as e:
    print(e)
