from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import actions

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

web = webdriver.Chrome(options=options)
wait = WebDriverWait(web,10)

actions.login(web)
time.sleep(3)
if(web.current_url == 'https://feralclans.com/news.php'):
    try:
        actions.claim_news(web)
    except:
        pass

while(True):
    stats = actions.generate_report(web)
    if(stats[1][-5:-2] == "100"):
        if(stats[1][-5:-4]!='('):
            willp = int(stats[1][-5:-2])
        else:
            willp = int(stats[1][-4:-2])
        if(willp>10):
            actions.train(web)

    time.sleep(60)
