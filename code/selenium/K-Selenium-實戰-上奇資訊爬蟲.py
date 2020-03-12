from selenium import webdriver
import os
from urllib.request import urlretrieve
import urllib           #網頁的操作(儲存.讀取...等)

driverPath = "C:\Program Files (x86)\chromedriver\chromedriver.exe"   # !!!一定要有driver
browser = webdriver.Chrome(driverPath)
url = 'http://www.grandtech.info/'
browser.get(url)

imgUrl = []
imgList = browser.find_elements_by_tag_name("img")
for i in range(len(imgList)):
    imgUrl.append(imgList[i].get_attribute("src"))

outFile = "圖檔 - OUTPUT - 上奇資訊網站爬蟲"

if os.path.exists(outFile) == False:
    os.mkdir(outFile)

for i in range(len(imgUrl)):
    print(imgUrl[i])
    local = os.path.join(outFile, os.path.basename(imgUrl[i]))
    """
    !!!用join將存檔位址完整結合
    但搜尋到的圖片可能位於其他子資料夾,其前方有"目錄路徑"
    basename可忽略"目錄路徑"而傳回程式檔名(才不會在outFile下開啟不存在的資料夾而發生錯誤)
    """
    """
    !!!!這是selenium的爬蟲(best),與response的爬蟲不一樣(不用以10240byte迴圈迭代寫入)
    只要: 先open -> 讀 -> 再寫入 即可
    """
    html = (urllib.request.urlopen(imgUrl[i]))
    data = html.read()
    f = open(local, 'wb')
    f.write(data)
    f.close()
browser.close()
"""
https://blog.csdn.net/seanwang_25/article/details/43317147
https://easonhan007.gitbooks.io/selenium-webdriver/content/29/download.py.html
https://zhuanlan.zhihu.com/p/27641546
"""