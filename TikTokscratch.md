將學習python APP爬蟲的內容記錄下來，以後方便使用

內容包含工具的簡介、抓包方法、bluezz旅遊筆記本爬取實例、移動裝置自動化、抖音短視頻爬取實例，以及我學習時踩到的大坑

使用到的工具：

    抓包工具 - fiddler,mitmproxy
    自動化工具 - appium
    Android 開發套件  - android sdk
    Android 模擬器 - 夜神模擬器 

 1. 抓包

python 網路爬蟲爬取網頁數據可以由 Requests 模組，再加上 Beautiful Soup解析下，就能簡單地獲得網頁上的資訊了。若想爬取APP的資訊，雖然數據通常是 json格式資料，可以直接以python內的字典型態存取並統計資料，但是獲取資料時，就必須使用抓包工具

抓包就是將網路傳輸、發送的數據進行截獲、編輯、儲存的操作

fiddler 抓包工具 ：

圖片 [拖曳以移動] ​圖片​


這頁的元素有幾張圖，圖會連結到另一個頁面，以及圖底下的文字

在抓包時，都有在fiddler上顯示(如圖  pic/ subject/ url)

如果想要在使用Google Chrome瀏覽器抓包，可以用擴展插件 SwitchyOmega

✳若是HTTPS請求

1. Tools -> Options -> HTTPS -> Decrypt HTTPS traffic

2. 打開瀏覽器 -> 輸入 [Proxy主機]:[Proxy通訊埠] -> 下載FiddlerRoot certificate

(模擬器/手機) 檢查 -> 安全性 ->信任的憑證 -> DO_NOT_TRUST_FiddlerRoot

這時候就可以抓取到HTTPS請求了

模擬器/手機 的設置：

設定 -> WIFI -> 修改網路 -> 進階 -> Proxy手動設定 ->輸入主機名稱、通訊埠->儲存

這樣就能正常使用fiddler抓包手機/模擬器了


mitmproxy 抓包工具：

mitmproxy(中間代理人工具)用來攔截、修改、保存 HTTP/HTTPS的請求，與fiddler不同的是以命令列終端的形式顯示，以及可以透過python控制請求、選擇保存特定的數據

安裝 mitmproxy ： (windows)

先安裝 Microsoft Visual C++ V14.0，否則報錯

https://visualstudio.microsoft.com/zh-hans/downloads/ -> 更早的下載項 -> 可轉散發套件及建置工具 -> Microsoft Build Tools 2015 Update 3

打開CMD

pip install mitmproxy

Windows不支援 mitmproxy這個命令

輸入mitmdump 開始抓包

Ctrl + C 可退出

若要指定端口號


mitmdump -p [端口號]

(手機/模擬器) 憑證下載：

在執行 mitmdump情況下

打開瀏覽器 -> mit.it -> Android(若是安卓手機/模擬器) -> 在手機上安裝憑證

手機安裝憑證的方法每個裝置會有些許差異，以及細節可能不太一樣

安裝下載的憑證：

設定 -> 安全性 -> 從SD卡安裝 -> 選擇下載的憑證 ->為這個憑證命名 ->確認

以上，mitmdump能夠正常使用了，再來就是導入python程式。

def response(flow):

...................

...................

...................


固定的寫法，用一個函式

固定的寫法只是必須要有這些函式名，還是可以放進類別中、進行封裝等等

函式的名稱為事件的名稱


    response 為服務端的響應(成功)被讀取
    request 為客戶端的請求(成功)被讀取
    error 為HTTP錯誤(伺服器無回應、連線問題等)


flow常用的用法

flow.request.headers   請求頭的資訊

flow.request.url       請求地址

flow.request.method    請求方式

flow.request.get_text() body中的內容

flow.response.text     返回內容


若想爬取一個固定的頁面，可以先找出那個頁面的網址(使用抓包工具)

例如某個APP的個人頁面網址均為  certainApp/user/data/userID

那就可以將certainApp/user/data這部分加入過濾的條件

def response(flow):

if TARGET_URL in flow.request.url:

...................

...................

...................

這樣就可以針對目標的存取了​

導入python執行mitmdump的指令：

cmd 移動至python檔案目錄下-> mitmdump -s (python檔案名稱) -p(端口號)

額外加入一個填坑(與APP爬蟲無關)：

通常過濾後就是要整理資料了，APP的資料通常是json形式，那就有很大的機會會使用到 python中解析 json的json_loads


json_data = json.loads(str_data,strict = 'false')

若爬取的資料有規定外的字符串就會報錯，而為了讓爬取時，避免因為這個問題讓程序終止，加入參數(strict = 'false')，就不會被原本嚴格控制內部字符串的限制約束了

 2. bluezz旅遊筆記本爬取實例 - 台北景點

有了抓包工具，就可以來爬取數據了

用fiddler找尋台北景點這個頁面的URL

圖片

觀察fiddler截獲的資料，找到爬取的目標

目標是這個頁面：

圖片​


我選擇了一個頁面元素較簡單的來練習，不用花太多時間解析~

有一部分的APP這樣就能爬取了


import requests

url = 'https://bluezz.tw/scenic.php?city=taipei'

header = {

(get your headers by fiddler)

}

res = requests.get(url,headers = header)

html = res.text


#爬取到的是html，開始解析


from bs4 import BeautifulSoup

soup =  BeautifulSoup(html, 'html.parser')

city = soup.find('link').get('href').replace("https://bluezz.tw/scenic.php?city=",'') #城市名

print(city)

li = soup.find_all('li')

for i in li:
    print(i.find('a').get('href'),i.text)


Output result:

'taipei'

https://data.bluezz.tw/c.php?id=25147 二子坪步道data

https://data.bluezz.tw/c.php?id=25870 天后宮data4.6

https://data.bluezz.tw/c.php?id=30276 臺北市鄉土教育中心(剝皮寮歷史街區)data

https://data.bluezz.tw/c.php?id=30400 臺北啤酒工廠(原建國啤酒廠)data

https://data.bluezz.tw/c.php?id=30606 蒲添生故居data

https://data.bluezz.tw/c.php?id=25142 優人神鼓山上劇場data

https://data.bluezz.tw/c.php?id=30423 五指山系- 白鷺鷥山、康樂山、明舉山親山步道data

https://data.bluezz.tw/c.php?id=25982 錢穆故居data

https://data.bluezz.tw/c.php?id=29783 國立臺灣工藝研究發展中心臺北當代工藝設計分館data4.4

https://data.bluezz.tw/c.php?id=30292 郭元益糕餅博物館data4.1

https://data.bluezz.tw/c.php?id=30307 草山行館data

https://data.bluezz.tw/c.php?id=27465 國史館data

https://data.bluezz.tw/c.php?id=26602 402號公園data

https://data.bluezz.tw/c.php?id=30277 北門-承恩門data4.4

https://data.bluezz.tw/c.php?id=27009 大屯遊憩區data4

 3. android SDK - UIAutomatorViewer


UIAutomatorViewer是一個用來定位APP元素的定位工具，於SDK中tools\bin目錄

打開 uiautomatorviewer.bat 開啟 UIAutomatorViewer


確認裝置是否連接：


cmd輸入 adb devices


使用UIAutomatorViewer就可以獲取頁面元素的定位，屬性資訊了，但只限於靜態頁面

在抓取其他動態頁面時，會出現這個報錯


Error while obtaining UI hierarchy XML file: com.android.ddmlib.SyncException: Remote object doesn't exist!


這個工具網路上有很多二次開發的版本，就可以獲取到動態頁面的元素資訊了，也同時使獲取的速度加快

而且原版有各式各樣一大堆報錯


圖片​


這是我使用的二次開發版本



 4.Appium

Appium是一個開源工具，用於自動化iOS移動設備，Android移動設備和Windows桌面平台上的本機，移動Web和混合應用程序

可以在不同平台上，用一套API來編寫測試案例

client端發送腳本至 appium服務器上，appium服務器將指令轉換成UIAutomator的命令，並與安卓上的bootstrap.jar進行TCP的連線，傳送命令


在爬取抖音用戶信息這個程序中，我們需要使用appium來進行模擬滑動


安裝後簡單設置一下測試


start sever -> Start Inspector Session -> Desired Capabilities -> 設置 platformName,  platformVersion, deviceName, appPackage, appActivity, noReset -> 其中 appPackage, appActivity 可由安卓SDK獲取 -> Start Session


Start Session後App會開啟(在已解鎖手機的情況下)


安卓SDK 確認安卓裝置是否連線


cmd -> adb devices


 5. APP爬蟲與自動化控制的架構



圖片​



利用appium，執行python腳本就可以控制手機，腳本根據要爬取的目標來編寫，目標的各項屬性通過UIAutomator查詢、定位


腳本控制安卓手機操作App，連線時由mitmproxy攔截


為什麼有抓包工具了還需要移動裝置自動化????


在請求頭中，會帶有一些關於裝置，或帳戶的字符(請求方式、裝置ID、版本名稱、作業系統、各種id、時間戳)，每次請求時，這些必須附帶的字串會不一樣，若無法知道他變換的邏輯，那就無法只靠一支python程式加上抓包取得的網址爬取數據，所以需要appium控制安卓真正地去使用這個APP，並在連線中抓包攔截。


例如： 請求youtube首頁時的請求頭

POST
Host:
Connection:
Content-Length:
X-Goog-Visitor-Id:
Content-Type:
X-Goog-Device-Auth:
X-GOOG-API-FORMAT-VERSION:
Authorization:
User-Agent:

需要這些字串附帶，才能正常請求




 6. 腳本的編寫

from appium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

#若未安裝，先用pip安裝

cap = {

  "platformName":

  "platformVersion":

  "deviceName":

  "appPackage":

  "appActivity":

  "noReset":

}

#appium set

#get appPackage,appActivity by SDK

driver = webdriver.Remote("http://localhost:{port}/wd/hub",cap)


安裝Appium客戶端


pip install Appium-Python-Client


安裝selenium(使用selenium中的WebDriverWait進行等待)


pip install selenium


寫好driver物件後，就可以使用這個物件的方法來編寫腳本了


driver.find_element_by_{ 屬性 }({Get through UIAutomator})


屬性有 id,classname,xpath等等，從UIAutomator獲取


若不加入等待，有時候App還沒載入好，腳本就進行下一步點擊了，所以需要設置等待時間，若超過這個等待時間，還未達成設定的條件，就會報錯

這樣寫可以讓腳本準確點擊，或因超時報錯，不至於點擊到其他地方


WebDriverWait(driver,10).until(....)

#單位是秒，不是毫秒


until(....)裡面可以放像是button上的文字，這樣如果不是這個button，就不會點擊了~

還有另一個方法是 until_not就是等待後，不成立則執行

if  WebDriverWait(driver,10).until(lambda x: "返回" in driver.find_element_by_id("ID of Button").text):

..............

這樣就能等待，並判斷"返回"這個按鈕是否有出現在畫面上了​


WebDriverWait這個方法不是強制的等待，若條件一滿足，就立即執行

相較於這個方法，若要實施強制的等待(不論條件有無滿足都必須等待)，就直接用sleep方法就好，讓等待程序在腳本裡


from time import sleep:

sleep(3)


獲得視窗的大小


driver.get_window_size()['width']

driver.get_window_size()['height']


滑動


driver.swipe(x,y,end_x,end_y)

time.sleep(1)

#通常搭配sleep


還有很多操作(多點的擊、長按、鍵盤控制)

https://pypi.org/project/Appium-Python-Client/


使用例外處理、等待，可以讓腳本不那麼容易出問題~


 7. 抖音短視頻爬取實例


透過上面的工具，編寫程式

(1) mitmproxy抓包 --->在抖音用戶個人頁面上抓取"關注"這個列表

(2) 解析原始資料 --->個人頁面上"關注"是一個列表，json格式，因此幾乎不需要解析

(3) 腳本運行 ---> 開啟抖音短視頻-> 先搜尋一個個人頁-> 從那個個人頁開始，找他有關注的人->點擊他 ->再搜尋他的個人頁 ........


抓包，只獲取個人頁面上的關注列表(關注列表的頁面)


圖片​



https://i.gyazo.com/449709424d490b862ec8d376d1733370.gif https://i.gyazo.com/449709424d490b862ec8d376d1733370.gif https://i.gyazo.com/449709424d490b862ec8d376d1733370.gif https://i.gyazo.com/449709424d490b862ec8d376d1733370.gif https://i.gyazo.com/449709424d490b862ec8d376d1733370.gif https://i.gyazo.com/449709424d490b862ec8d376d1733370.gGIF想直接放上來，但好像顯示不出來，用鏈結吧~

https://i.gyazo.com/12acd93d5e37bc1f63755d83c8806c5f.gif

這個是滑動，請求完整的用戶列表

https://i.gyazo.com/a01114a69e9f308b487057b33b1d6147.gif

https://i.gyazo.com/20cdaa13f290afa86ade489e251d260d.gif

點擊列表中的用戶，再點擊關注，繼續爬取


最後把他們的UID存儲下來 用記事本

Output result:

92438491697
108716622809
83075809131
98029790685
106102063975
3408083110344600
76322662982
58713807451
58910726039
111426814781
..

.

.

.

數量很多，擷取一點點~ 這個頁面包含個人頁的基本信息，這裡就不再爬取了


