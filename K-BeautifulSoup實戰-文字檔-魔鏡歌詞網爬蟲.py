import bs4 , requests, os , re
"""
魔鏡歌詞網爬蟲
"""

def songCrawler(url):
    print("輸入歌手的歌單頁面,可將所有歌曲顯示出來:")
    htmlFile = requests.get(url)
    print("網頁下載中")
    htmlFile.raise_for_status()
    print("網頁下載完成")
    objSoup = bs4.BeautifulSoup(htmlFile.text, "lxml")
    '''
    命名解釋:
        name:歌手的串列/singerName:歌手的字串
        song:歌的串列/songNew:歌詞的字串
        songFin:處理掉一些多餘的標籤.雜訊之後的歌詞字串
    '''
    name = objSoup.select("dd.hb9")
    singerName = name[0].text
    singerName = "\n"+str(singerName)
    song1 = objSoup.select("span.hc3")           #表格第一行的歌詞
    song2 = objSoup.select("span.hc4")           #表格第二行的歌詞(song1/2不同標籤下,分開處理)
    songNew1 = []
    songNew2 = []

    for i in range(1,len(song1)):
        songNew1.append(song1[i].text)

    for i in range(1,len(song2)):
        songNew2.append(song2[i].text)

    songFin2 = "".join(songNew2)
    songFin2 = str(songFin2)

    pattern2 = "\n"
    pattern_2 = r"[0-9]+."

    songFinal2 = re.sub(pattern2, "", songFin2)
    songFinal2 = re.sub(pattern_2, "/", songFinal2)
    songFinal2 = re.sub("/", pattern2, songFinal2)
    songFinal2 = songFinal2.rstrip()

    songFin1 = "".join(songNew1)        #用空字元將list完全黏成string
    songFin1 = str(songFin1)            #把"標籤字串"轉換成"字串"(變成純字串,才能用字串的函數.方法)

    pattern1 = r"[0-9]+."               #用Regex把歌曲前編號刪除

    songFinal1 = re.sub(pattern1, "\n", songFin1)
    print(singerName +"\n" + songFinal1 + songFinal2)

def lyricsCrawler(url):
    print("輸入一首歌的歌詞頁面,可將所有的歌詞顯示出來:")
    htmlFile = requests.get(url)
    print("網頁下載中")
    htmlFile.raise_for_status()
    print("網頁下載完成")
    objSoup = bs4.BeautifulSoup(htmlFile.text, "lxml")
    """
    命名解釋:
        name:歌名的串列/word:歌名的字串
        lyrics:歌詞的串列/string:歌詞的字串
        stringNew:處理掉一些多餘的標籤.雜訊之後的歌詞字串
    """
    name = objSoup.select("dt#fsZx2,.fsZx2")
    lyrics = objSoup.select("dd#fsZx3,.fsZx3")  #!!!要連在一起,因為同一個節點(此句用逗號分隔,意指同時鎖定id與class等屬性)

    word = str(name[0].text).lstrip()       #將開頭的空白.換行等清空
    string = str(lyrics[0])

    stringNew = re.sub("<br/>", "\n", string)
    stringNew = re.sub(r"(<dd class=)\"(\w)+\"\s(id=)\"(\w)+\">", "", stringNew)
    stringNew = re.sub(r"\[\d+:\d+\.\d+\].*", "", stringNew)  # 將重複的歌詞.雜訊取代為空行
    stringNew = re.sub(r"<ol>.*|</dd>", "", stringNew)        # 同上句
    stringFin = "\n" + word + stringNew

    print(stringFin.rstrip())           #將結尾的空白.換行等清空

lyricsCrawler("https://mojim.com/twy104500x26x1.htm")
songCrawler("https://mojim.com/twh158291.htm")

