from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys
def get_size():
  w = driver.get_window_size()['width']
  h = driver.get_window_size()['height']
  return(w,h)
cap = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.ss.android.ugc.aweme",
  "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
  "noReset": True
}
#com.ss.android.ugc.aweme/.splash.SplashActivity
driver = webdriver.Remote("http://localhost:4723/wd/hub",cap)
key = str(input('Enter search seed'))
## seed setting
#搜索按鈕
if WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("com.ss.android.ugc.aweme:id/bnx")):
    driver.find_element_by_id("com.ss.android.ugc.aweme:id/bnx").click()
#搜索框
if WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("com.ss.android.ugc.aweme:id/ahw")):
    driver.find_element_by_id("com.ss.android.ugc.aweme:id/ahw").send_keys(key) 
    #輸入
    while driver.find_element_by_id("com.ss.android.ugc.aweme:id/ahw").text != key:
        driver.find_element_by_id("com.ss.android.ugc.aweme:id/ahw").send_keys(key)
        time.sleep(0.1)
    #點選搜尋
    if WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("com.ss.android.ugc.aweme:id/ffy")):
        driver.find_element_by_id("com.ss.android.ugc.aweme:id/ffy").click()
    #點選人物
        if WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("com.ss.android.ugc.aweme:id/c1i")):
            driver.find_element_by_id("com.ss.android.ugc.aweme:id/c1i").click()
        #點選關注
        try:
            if WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("com.ss.android.ugc.aweme:id/b1m")):
                driver.find_element_by_id("com.ss.android.ugc.aweme:id/b1m").click()
                driver.find_element_by
        except:
            print('Seeds cannot be used')
            sys.exit()
        #slip
        for times in range(10):
            l = get_size()
            x1 = int(l[0]*0.5)
            y1 = int(l[0]*0.9)
            y2 = int(l[0]*0.15)
            if WebDriverWait(driver,10).until(lambda x:"关注" in  driver.find_element_by_id("android:id/text1").text):
                while True:
                    if '没有更多了' in driver.page_source:
                        break
                    driver.swipe(x1,y1,x1,y2)
                    time.sleep(0.6)
            else:
                print('Seeds error')
                sys.exit()
            #點擊下方的用戶
            for i in range(9,0,-1):
                if WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout["+str(i)+"]/android.widget.LinearLayout[1]")):
                    driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout["+str(i)+"]/android.widget.LinearLayout[1]").click()
                    driver.implicitly_wait(5)
                    if WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("com.ss.android.ugc.aweme:id/b1m")):
                        driver.find_element_by_id("com.ss.android.ugc.aweme:id/b1m").click()
                        if "关注" in  driver.find_element_by_id("android:id/text1").text:
                            break 
                else:
                    if WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.ss.android.ugc.aweme:id/kp' and @content-desc='返回']")):
                        driver.find_elements_by_xpath("//android.widget.ImageView[@resource-id='com.ss.android.ugc.aweme:id/kp' and @content-desc='返回']").click()
else:
    print("there is no searching button")