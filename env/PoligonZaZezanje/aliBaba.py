from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from joblib import Parallel,delayed
from locators import *
from methods import *


def sellerScript(link):

    driver = webdriver.Chrome()
    driver.get(link)
    driver.set_window_size(1440, 900)
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, signIn).click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, userId).send_keys('sanda86posao@gmail.com')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, password).send_keys('Flower08091986')
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, LogIn).click()
    # driver.find_element(By.CSS_SELECTOR,'#DashSortByContainer > ul.sel > li > div > a').click()
    # time.sleep(5)
    # driver.find_element(By.CSS_SELECTOR,'#SortMenu > li:nth-child(3) > a').click()
    time.sleep(5)
    items = driver.find_elements(By.CSS_SELECTOR, singleItem)
    duzina_liste_itema = len(items)
    print('lista ima ' + str(duzina_liste_itema) + ' clanova')
    wait = WebDriverWait(driver, 5)
    # pageBid(duzina_liste_itema=duzina_liste_itema, driver=driver, wait=wait)
    startFrom = 15
    pageSol(driver=driver, duzina_liste_itema=duzina_liste_itema, wait=wait, n=startFrom)




# urls = ['https://www.ebay.com/sch/dancingqueen_wg/m.html?_nkw=&_armrs=1&_ipg=&_from=&rt=nc&LH_Auction=1']
# Parallel(n_jobs=-3)(delayed(sellerScript(link=url))(url) for url in urls) #execute parallel for all urls
url='https://www.ebay.com/sch/dancingqueen_wg/m.html?_nkw=&_armrs=1&_ipg=&_from=&rt=nc&LH_Auction=1'
sellerScript(link=url)
