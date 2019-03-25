import time
from locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# def pagesBid(duzina_liste_itema,driver,wait,):
    # n = 0
    # singlePage(duzina_liste_itema=duzina_liste_itema,driver=driver,wait=wait,n=n)

def pageSol(driver,duzina_liste_itema, wait, n):
    print(n)
    pageLength = len(forPageLength)-4
    print('ovo je page length ' + str(pageLength))
    time.sleep(1)
    for p in range(1, pageLength):
        singlePageLocator = '#Pagination > tbody > tr > td.pages > a:nth-child(' + str(p) + ')'
        time.sleep(1)
        print('ovo je single page locator ' + str(singlePageLocator))
        singlePage(duzina_liste_itema=duzina_liste_itema, driver=driver, wait=wait, n=n)
        driver.find_element(By.CSS_SELECTOR, singlePageLocator).click()


def singlePage(duzina_liste_itema, driver, wait, n):
    for i in range(n, duzina_liste_itema):
        print('upravo biduje za ' + str(i) + ' clan')
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.sresult.lvresult.clearfix.li h3.lvtitle')))
        element1 = driver.find_elements(By.CSS_SELECTOR, 'li.sresult.lvresult.clearfix.li h3.lvtitle')[i].click()
        element1
        try:
            element1
        except:
            pass
        # time.sleep(2)
        curBidString = driver.find_element(By.CSS_SELECTOR, currentBidAmount).text
        curBid = float(curBidString[4:])
        print('ovo je trenutan bid na elementu ' + str(curBid))
        if curBid < 0.3:
            print('za ovaj treba bidovati')
            clickOnBid(wait=wait,driver=driver)
        else:
            print('bezi dalje')
        time.sleep(3)
        driver.back()
        time.sleep(2)
        # driver.back()
        # time.sleep(3)
        # driver.back()
        # time.sleep(5)

def clickOnBid(wait,driver):

    element1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#MaxBidId')))
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#MaxBidId').send_keys('0.3')
    time.sleep(5)
    print('a')
    driver.find_element(By.CSS_SELECTOR, '#bidBtn_btn').click()
    print('b')
    time.sleep(5)
    try:
        driver.find_element(By.CSS_SELECTOR, '#w1-28-_reviewBidSec_btn').click()
        print('c')
    except:
        pass
    try:
        driver.find_element(By.CSS_SELECTOR, '#w1-29-_reviewBidSec_btn').click()
        print('d')
    except:
        pass
    try:
        driver.find_element(By.CSS_SELECTOR, '#w1-30-_reviewBidSec_btn').click()
        print('e')
    except:
        pass
    try:
        driver.find_element(By.CSS_SELECTOR, '#w1-31-_reviewBidSec_btn').click()
        print('f')
    except:
        pass
    try:
        driver.find_element(By.CSS_SELECTOR, '#w1-32-_reviewBidSec_btn').click()
        print('g')
    except:
        pass
    try:
        driver.find_element(By.CSS_SELECTOR, '#w1-33-_reviewBidSec_btn').click()
        print('h')
    except:
        pass
    time.sleep(5)
    if driver.find_element(By.CSS_SELECTOR, "#vi_oly_powerBid > div > div.clz > div > div").is_displayed():
        driver.find_element(By.CSS_SELECTOR, "#vi_oly_powerBid > div > div.clz > div > div").click()
        print('modal za poboljsanje ponude se pojavio')
    else:
        pass
        print('modal za poboljsanje ponude nije se pojavio')
    if driver.find_element(By.CSS_SELECTOR, '#w1-5-_msg').is_displayed():
        print('vidi se text da si highest bidder na ovom itemu')
        driver.execute_script('document.querySelector("#smtBackToAnchor").click()')
    else:
        pass
    try:
        driver.find_element(By.CSS_SELECTOR,'#vi_oly_powerBid > div > div.clz > div > div').click()
        print('modal za poboljsanje ponude se pojavio')
        print('f')
    except:
        print('modal za poboljsanje ponude nije se pojavio')
        pass