from selenium import webdriver
import os

"""
目標:爬取成大校網的新聞.公告.活動的標題.連結.圖
"""
driverPath = "C:\Program Files (x86)\chromedriver\chromedriver.exe"   # !!!一定要有driver
browser = webdriver.Chrome(driverPath)
url = 'http://web.ncku.edu.tw/bin/home.php'
browser.get(url)

outFile = "圖+文字檔 - OUTPUT - 成大校網資訊爬蟲"

if os.path.exists(outFile) == False:
    os.mkdir(outFile)

dynamicNews = browser.find_elements_by_xpath("//div[@id='myCarousel']//a/img")    #!!!注意:屬性用'單引號'包住
print("-------------成大動態新聞快報-------------")
for i in range(len(dynamicNews)):
    print(dynamicNews[i].get_attribute("alt"))

print("--------------成大研發快訊---------------")
staticNewsTitle = browser.find_element_by_xpath("//div[@class='h3 RD-title']/a")
staticNewsTitle2 = browser.find_element_by_xpath("//div[@class='h4 RD-content']")
staticNewsContent = browser.find_element_by_xpath("//div[@class='RD-content']")
print(staticNewsTitle.text+"\n from"+staticNewsTitle2.text+"\n content: "+staticNewsContent.text)

print("----------------成大公告-----------------")
postDate = browser.find_elements_by_xpath("//div[@class='h5']/span[@class='date ']")
postTitle = browser.find_elements_by_xpath("//div[@class='h5']/a")
for i in range(len(postDate)):
    print(postDate[i].text," ",postTitle[i].text)

"""
print("--------------成大活動資訊----------------")    #失敗,因為其為動態資料

activityTitle = browser.find_elements_by_xpath("//h4[@class='activity_name']/a")
activityTime = browser.find_elements_by_xpath("//div[@class='post.span4']//p[@class='time']")
activityPlace = browser.find_elements_by_xpath("//div[@class='post.span4']//p[@class='place']")
print(len(activityPlace))
print(len(activityTime))
print(len(activityTitle))
for i in range(len(activityTitle)):
    print(activityTitle[i].text,"\n",activityTime[i].text," ",activityPlace[i].text)
"""