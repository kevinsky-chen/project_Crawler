from selenium import webdriver
import os , time
#from urllib.request import urlretrieve
from selenium.webdriver.support.ui import Select     #可操作下拉選單
import urllib           #網頁的操作(儲存.讀取...等)

driverPath = "C:\Program Files (x86)\chromedriver\chromedriver.exe"   # !!!一定要有driver
browser = webdriver.Chrome(driverPath)
url = 'http://railway.hinet.net/Foreign/TW/index.html'         #台鐵網路訂票系統官網
browser.get(url)
outFile = "資料 - OUTPUT - 台鐵訂票爬蟲"

clickEle = browser.find_element_by_link_text("訂去回票")
time.sleep(1)
clickEle.click()
clickEle1 = browser.find_element_by_link_text("車次訂去回票")
time.sleep(1)
clickEle1.click()

print("車次訂去回票")
print("身分證字號")
id = browser.find_element_by_id("person_id")
myID = input()
id.send_keys(myID)
id.submit()
browser.back()        #往回一頁

print("這些是起站代碼,請選擇一個起始站:")
select = Select(browser.find_element_by_css_selector('[name = from_station]'))
for op in select.options:
    print(op.text)              #將起站代碼全部顯示
#fromStation = input("請輸入起始站代碼")
#select.select_by_value(fromStation)
fromStation = input("請輸入起始站: e.g.:100-台北\n")
select.select_by_visible_text(fromStation)       #填入起站的下拉選單

print("這些是到站代碼,請選擇一個終點站:")
select2 = Select(browser.find_element_by_css_selector('[name = to_station]'))
for op in select2.options:
    print(op.text)              #將起站代碼全部顯示
#toStation = input("請輸入終點站代碼")
#select2.select_by_value(toStation)
toStation = input("請輸入終點站: e.g.:100-台北\n")
select2.select_by_visible_text(toStation)   #填入到站的下拉選單

print("這些是去程乘車日期:")
select5 = Select(browser.find_element_by_id('getin_date'))
for op in select5.options:
    print(op.text)
getinDate = input("請選擇一天去程乘車日期: e.g.:2018/06/26【二】\n")
select5.select_by_visible_text(getinDate)   #填入

print("這些是回程乘車日期:")
select6 = Select(browser.find_element_by_id('getin_date2'))
for op in select6.options:
    print(op.text)
getoutDate = input("請選擇一天回程乘車日期: e.g.:2018/06/27【三】\n")
select6.select_by_visible_text(getoutDate)   #填入

fromTicket = input("請輸入去程訂票張數:")
select3 = Select(browser.find_element_by_id('order_qty_str'))
select3.select_by_visible_text(fromTicket)

toTicket = input("請輸入回程訂票張數:")
select4 = Select(browser.find_element_by_id('order_qty_str2'))
select4.select_by_visible_text(toTicket)

trainNO = browser.find_element_by_id("train_no")
train1 = input("請輸入去程車次代碼:")
trainNO.send_keys(train1)
trainNO.submit()
browser.back()        #往回一頁

trainNO2 = browser.find_element_by_id("train_no2")
train2 = input("請輸入回程車次代碼:")
trainNO2.send_keys(train2)
trainNO2.submit()


"""
!!!用join將存檔位址完整結合
但搜尋到的圖片可能位於其他子資料夾,其前方有"目錄路徑"
basename可忽略"目錄路徑"而傳回程式檔名(才不會在outFile下開啟不存在的資料夾而發生錯誤)
"""
"""
!!!!這是selenium的爬蟲(best),與response的爬蟲不一樣(不用以10240byte迴圈迭代寫入)
只要: 先open -> 讀 -> 再寫入 即可
"""
"""
randomPicPwd = browser.find_element_by_id("idRandomPic")
browser.get(browser.current_url)
print(browser.current_url)
browser.get_screenshot_as_file('example.png')
randomPic = input("圖片驗證檢查,請輸入圖形中的英數字:\n")
randomPicPwd.submit()
"""
#img = browser.find_element_by_css_selector("img#idRandomPic")
#imgUrl = img.get_attribute("src")
#print(browser.current_url)
#browser.save_screenshot(browser.current_url)
#imgEle = urllib.request.urlopen(browser.current_url)
"""
local = os.path.join(outFile, "random.png")
data = imgEle.read()
f = open(local, 'wb')
f.write(data)
f.close()
"""

print("請自行輸入驗證碼:")
time.sleep(3)
print("訂票成功")
