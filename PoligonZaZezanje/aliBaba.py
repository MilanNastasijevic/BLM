from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get('https://www.ebay.com/sch/liliang1987one/m.html?_nkw=&_armrs=1&_ipg=&_from=&rt=nc&LH_Auction=1')
driver.set_window_size(1440,900)
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,'#gh-ug > a').click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,'#userid').send_keys('sanda86posao@gmail.com')
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'#pass').send_keys('Flower08091986')
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR,'#sgnBt').click()
# driver.find_element(By.CSS_SELECTOR,'#DashSortByContainer > ul.sel > li > div > a').click()
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,'#SortMenu > li:nth-child(3) > a').click()
time.sleep(5)
items = driver.find_elements(By.CSS_SELECTOR,'li.sresult.lvresult.clearfix.li h3.lvtitle')
duzina_liste_itema = len(items)
print('lista ima ' + str(duzina_liste_itema) +' clanova')
wait = WebDriverWait(driver, 5)
for i in range(37,duzina_liste_itema):

    print('upravo biduje za ' + str(i) + ' clan')
    time.sleep(5)
    element = driver.find_elements(By.CSS_SELECTOR, 'li.sresult.lvresult.clearfix.li h3.lvtitle')[i].click()

    element1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#MaxBidId')))
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,'#MaxBidId').send_keys('0.3')
    time.sleep(5)
    print('a')
    driver.find_element(By.CSS_SELECTOR,'#bidBtn_btn').click()
    print('b')
    time.sleep(5)
    try:
        driver.find_element(By.CSS_SELECTOR,'#w1-28-_reviewBidSec_btn').click()
        print('c')
    except:
        pass
    try:
        driver.find_element(By.CSS_SELECTOR,'#w1-29-_reviewBidSec_btn').click()
        print('d')
    except:
        pass
    try:
        driver.find_element(By.CSS_SELECTOR,'#w1-30-_reviewBidSec_btn').click()
        print('e')
    except:
        pass
    try:
        driver.find_element(By.CSS_SELECTOR,'#w1-31-_reviewBidSec_btn').click()
        print('f')
    except:
        pass
    try:
        driver.find_element(By.CSS_SELECTOR,'#w1-32-_reviewBidSec_btn').click()
        print('g')
    except:
        pass
    time.sleep(15)
    try:
        driver.execute_script("('div.clzBtn').click()")
        print('modal za poboljsanje ponude se pojavio')
    except:
        pass
        print('modal za poboljsanje ponude nije se pojavio')
    # try:
    #     driver.find_element(By.CSS_SELECTOR,'#vi_oly_powerBid > div > div.clz > div > div').click()
    #     print('f')
    # except:
    #     pass
    time.sleep(3)
    driver.back()
    time.sleep(2)
    # driver.back()
    # time.sleep(3)
    # driver.back()
    # time.sleep(5)
