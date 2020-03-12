from selenium import webdriver

driverPath = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"   # !!!一定要有driver
browser = webdriver.Chrome(driverPath)
url = 'http://www.taiwanlottery.com.tw/index_new.aspx'
browser.get(url)

#------下載最新一期的威力彩--------
print("最新一期威力彩:")
select = browser.find_elements_by_css_selector("div.ball_tx.ball_green")
normalSequence = select[0:6]
orderSequence = select[6:12]
print("依開出順序: ")
for i in range(len(normalSequence)):
    print(normalSequence[i].text, end=" ")
print("\n"+"依大小順序: ")
for i in range(len(orderSequence)):
    print(orderSequence[i].text,end=" ")
select2 = browser.find_elements_by_css_selector("div.ball_red")
print("\n第二期: \n"+select2[1].text)

#------下載最新一期的大樂透--------
print("\n最新一期大樂透:")
select3 = browser.find_elements_by_css_selector("div.ball_tx.ball_yellow")    #找填表單.搜尋列處
normalSequence = select3[20:26]
orderSequence = select3[26:32]
print("依開出順序: ")
for i in range(len(normalSequence)):
    print(normalSequence[i].text, end=" ")
print("\n"+"依大小順序: ")
for i in range(len(orderSequence)):
    print(orderSequence[i].text,end=" ")
print("\n特別期: \n"+select2[2].text)

