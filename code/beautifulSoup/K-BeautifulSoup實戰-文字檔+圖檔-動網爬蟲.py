import bs4 , requests, os , re , shutil
"""
:動網爬蟲:
漏洞:無法抓嵌入網站的圖片檔(e.g.:instagram...)
"""
outFile = "F:\Python projects\MyStudy\K-網路爬蟲\圖+文 - OUTPUT - 動網爬蟲"

if os.path.exists(outFile) == False:
    os.mkdir(outFile)


def regularSoup(url):
    htmlFile = requests.get(url)
    print("網頁下載中")
    htmlFile.encoding = "utf-8"         #設定網頁編碼格式
    htmlFile.raise_for_status()
    print("網頁下載完成")
    return htmlFile


def playersNewsCrawler(url):
    print("輸入關鍵字頁面,可將所有新聞(圖+文)抓取至資料夾:")
    htmlFile = regularSoup(url)                          #因為起始設定皆相同,所以寫成一個regularSoup,以簡短程式長度
    objSoup = bs4.BeautifulSoup(htmlFile.text, "lxml")

    news = objSoup.select("h3.jeg_post_title")          #抓新聞標題
    pageNumber = objSoup.select("span.page_info")       #抓搜尋頁碼

    w = objSoup.select("a.jeg_readmore")                #抓各篇新聞的網址
    for i in range(len(w)):
        web = w[i].get("href")                          #抓各篇新聞的網址
        #print(web)

        dirRout = "".join(outFile + "\\" + (news[i].text.lstrip()).rstrip() + " " + " Page" + pageNumber[0].text[3])
        os.mkdir(dirRout)

        regularSoup(web)
        htmlFile_under = regularSoup(web)               #為了各篇新聞能夠獨自分析而建立的soup物件
        objSoup_under = bs4.BeautifulSoup(htmlFile_under.text, "lxml")
        #print((news[i].text.lstrip()).rstrip())

        objTXT = objSoup_under.select("p")             #抓新聞裡的文字
        tmp = []
        for x in range(len(objTXT)):
            tmp.append(objTXT[x].text)
            #print(objTXT[x].text)
            #print(tmp)
            #print(len(objTXT))
            try:
                tmp[x].encode('cp950').decode('cp950')   #有可能發生編碼不相容等錯誤
            except UnicodeEncodeError:
                tmp[x] = " "                             #若有,將該字串以空白代替
        TXT = '\n'.join(tmp)

        with open(dirRout + "\\Article.txt", "a") as TXT_obj:
                TXT_obj.write(TXT)

        objImg = objSoup_under.select("img")            #抓新聞裡的圖片
        for i in range(len(objImg)):
            try:
                picUrl = (objImg[i].get("src"))     #得到src屬性下的內容
                print(picUrl)

                picture = requests.get(picUrl)      #把整段網址用get存入picture物件
                picture.raise_for_status()

                pattern = r"\.png|\.bmp|\.gif|\.jpeg|\.jpg"    #從網址裡找出其圖檔格式

                format = re.findall(pattern, str(picUrl))     #!!!記得:Regex搜的都是"字串string"
                formatFin = format[0]

                """
                if not format:                                                 #原想嘗試抓嵌入式網站的圖片
                    format = objSoup_under.select("img[data-type]")
                    formatFin = str(format[0].get("data-type"))
                    if  not format:
                        format = objSoup_under.select("img.EmbeddedMediaImage")
                        formatFin = re.findall(pattern, format[0].text)
                        formatFin = str(formatFin)
                """

                picFile = open(os.path.join(dirRout, str(i))+formatFin, "wb")

                """
                !!!用join將存檔位址完整結合
                但搜尋到的圖片可能位於其他子資料夾,其前方有"目錄路徑"
                basename可忽略"目錄路徑"而傳回程式檔名(才不會在outFile下開啟不存在的資料夾而發生錯誤)
                """

                for diskStorage in picture.iter_content(10240):
                    picFile.write(diskStorage)
                picFile.close()

            except:
                continue


playersNewsCrawler("https://www.dongtw.com/tag/lebron-james")