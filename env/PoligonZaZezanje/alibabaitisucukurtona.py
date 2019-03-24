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
time.sleep(10)
items = driver.find_elements(By.CSS_SELECTOR,'li.sresult.lvresult.clearfix.li h3.lvtitle')
duzina_liste_itema = len(items)
wait = WebDriverWait(driver, 10)
for i in range(35,duzina_liste_itema):
    time.sleep(15)
    element = driver.find_elements(By.CSS_SELECTOR, 'li.sresult.lvresult.clearfix.li h3.lvtitle')[i].click()

    element1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#MaxBidId')))
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,'#MaxBidId').send_keys('0.3')
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR,'#bidBtn_btn').click()
    time.sleep(15)
    try:
        driver.find_element(By.CSS_SELECTOR,'#w1-28-_reviewBidSec_btn').click()
    except:
        pass
    try:
        driver.find_element(By.CSS_SELECTOR,'#w1-29-_reviewBidSec_btn').click()
    except:
        pass
    try:
        driver.find_element(By.CSS_SELECTOR,'#w1-30-_reviewBidSec_btn').click()
    except:
        pass
    time.sleep(15)
    try:
        driver.find_element(By.CSS_SELECTOR,'#vi_oly_powerBid > div > div.clz > div > div').click()
    except:
        pass
    time.sleep(3)
    driver.back()
    time.sleep(2)
    driver.back()
    time.sleep(3)
    # driver.back()
    # time.sleep(5)
