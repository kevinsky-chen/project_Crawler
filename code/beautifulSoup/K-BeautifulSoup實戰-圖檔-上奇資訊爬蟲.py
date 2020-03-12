import bs4 , requests, os

url = "http://www.grandtech.info/"
htmlFile = requests.get(url)
print("網頁下載中")
htmlFile.encoding = 'utf8'
"""
因為原本requests 所下載的內容皆為unicode(unicode是為了讓程式語言可以處理各式各樣編碼)，
由於unicode 無法直接處理，所以我們要把取得的內容編碼成utf8才會是我們平常看到的中文字。
"""

htmlFile.raise_for_status()
print("網頁下載完成")
objSoup = bs4.BeautifulSoup(htmlFile.text, "lxml")

outFile = "圖檔 - OUTPUT - 上奇資訊網站爬蟲"
if os.path.exists(outFile) == False:
    os.mkdir(outFile)

objImg = objSoup.select("img")
for i in range(len(objImg)):
    preUrl = (objImg[i].get("src"))                  #得到src屬性下的內容
    print("%s 圖片下載中" % preUrl)
    proUrl = url + preUrl                            #再加上首頁網址 == 整段網址
    print("%s 圖片下載中" % proUrl)
    picture = requests.get(proUrl)                   #把整段網址用get存入picture物件
    picture.raise_for_status()
    print("%s 圖片下載完成" % picture)

    pictFile = open(os.path.join(outFile, os.path.basename(preUrl)), "wb")
    """
    !!!用join將存檔位址完整結合
    但搜尋到的圖片可能位於其他子資料夾,其前方有"目錄路徑"
    basename可忽略"目錄路徑"而傳回程式檔名(才不會在outFile下開啟不存在的資料夾而發生錯誤)
    """
    for diskStorage in picture.iter_content(10240):
        pictFile.write(diskStorage)
    pictFile.close()




