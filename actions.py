from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import random

user = ""
passwd = ""
attributes = ["str","agl","gua","lab"]

def login(web):
    web.get('https://feralclans.com/home.php')
    uf = web.find_element_by_xpath("//*[@id=\"login\"]")
    pf = web.find_element_by_xpath("//*[@id=\"password\"]")

    uf.send_keys(user)
    pf.send_keys(passwd)

    web.find_element_by_xpath("/html/body/div/section/article/div[1]/div[1]/div/div/span").click()

def claim_news(web):
    web.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div[5]/div[5]/img").click()

def train(web):
    web.get("https://feralclans.com/workcamp.php")
    time.sleep(3)
    with open("last_attr") as f:
        prev = f.read()
    n = (attributes.index(prev)+1)%4
    current = attributes[n]
    with open("last_attr","w") as f:
        f.write(current)

    if(current=="str"):
        print("as")
        web.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[3]/div[3]/div[1]/div/div").click()
    elif(current=="agl"):
        web.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[3]/div[3]/div[2]/div/div").click()
    elif(current=="gua"):
        web.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[3]/div[3]/div[3]/div/div").click()
    else:
        web.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[3]/div[3]/div[4]/div/div").click()

def generate_report(web):
    web.get("https://feralclans.com/home.php")

    time.sleep(3)
    energy = web.find_element_by_xpath('/html/body/div[2]/header/div[2]/div[1]/div[2]/div[1]/div[3]').text
    will = web.find_element_by_xpath('/html/body/div[2]/header/div[2]/div[1]/div[2]/div[3]/div[3]').text
    rage = web.find_element_by_xpath('/html/body/div[2]/header/div[2]/div[1]/div[2]/div[4]/div[3]').text
    adrenaline = web.find_element_by_xpath('/html/body/div[2]/header/div[2]/div[1]/div[2]/div[5]/div[3]').text

    infop1 = web.find_element_by_xpath('/html/body/div[2]/div/div[1]/table[2]/tbody/tr[1]/td[1]').text
    infop2 = web.find_element_by_xpath('/html/body/div[2]/div/div[1]/table[2]/tbody/tr[1]/td[2]').text
    infop3 = web.find_element_by_xpath('/html/body/div[2]/div/div[1]/table[2]/tbody/tr[2]/td[1]').text
    infop4 = web.find_element_by_xpath('/html/body/div[2]/div/div[1]/table[2]/tbody/tr[2]/td[2]').text
    infop5 = web.find_element_by_xpath('/html/body/div[2]/div/div[1]/table[2]/tbody/tr[3]/td[1]').text
    infop6 = web.find_element_by_xpath('/html/body/div[2]/div/div[1]/table[2]/tbody/tr[3]/td[2]').text

    stats = [energy,will,rage,adrenaline]
    return stats
