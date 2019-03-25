import locators, time, math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class pageMethods():

    def startPage(self, startIndex):
        if startIndex <= 100:
            print('jej')
        else:
            startOnPage = round((startIndex / 100) + 1)
            forItem = round(startIndex/100)
            startItemOnPage = (startIndex - forItem*100)

    def trasferThroughPages(self,driver, startPage):
        pages = driver.find_elements(By.CSS_SELECTOR, locators.forPageLength)
        lengthPages = len(pages)
        print(lengthPages)
        for page in range(startPage, lengthPages):
            driver.find_elements(By.CSS_SELECTOR, locators.forPageLength)[page].click()

    # def crossPages(self):

        #ovde treba da se definise kako ce preci na sledecu stranu, ali da ne pocne od clana liste startItemOnPage

class checkList():

    #ovde se pregleda lista itema po strani
    def findingItems(self, driver, startIndex):

        listOfItems = driver.find_elements(By.CSS_SELECTOR, locators.singleItem)
        lenListOfItems = len(listOfItems)
        for item in range(startIndex,lenListOfItems):
            time.sleep(10)
            driver.find_elements(By.CSS_SELECTOR, locators.singleItem)[item].click()
            print('upravo biduje za ' + str(item) + ' clan')
            curBidString = driver.find_element(By.CSS_SELECTOR, locators.currentBidAmount).text
            curBid = float(curBidString[4:])
            print('ovo je trenutan bid na elementu ' + str(curBid))
            if curBid < 0.3:
                print('za ovaj treba bidovati')
                wait = WebDriverWait(driver, 10)
                tryToBid().clickOnBid(wait=wait,driver=driver)
            else:
                print('bezi dalje')
            driver.find_element(By.CSS_SELECTOR, locators.backToList).click()

class biddingMethods():

#definisati sve metode neophodne za uspesno i provereno bidovanje

    def singleBid(self):
        print('biduje seee')

class pageForMethods():


    def trasferThroughPages(self, driver, startPage):
        pages = driver.find_elements(By.CSS_SELECTOR, locators.forPageLength)
        lengthPages = len(pages)
        print(lengthPages)
        for page in range(startPage, lengthPages):
            print('this is page' + str(page))
            time.sleep(1)
            driver.find_elements(By.CSS_SELECTOR, locators.forPageLength)[page].click()
            time.sleep(1)

    def additionalMethod(self,driver, startItem):
        pages = driver.find_elements(By.CSS_SELECTOR, locators.forPageLength)
        lengthPages = len(pages)
        print(lengthPages)
        startOnPage = math.floor((startItem / 25) + 1)
        forItem = round(startItem / 25 - 1)#ovde ti prikazuje -1 kad je pocetni 0
        
        startItemOnPage = (startItem - forItem * 25)
        print('startOnPage ' + str(startOnPage))
        print('forItem ' + str(forItem))
        print('startItemOnPage ' + str(startItemOnPage))
        print('this is page' + str(startOnPage))
        driver.find_elements(By.CSS_SELECTOR, locators.forPageLength)[startOnPage].click()
        time.sleep(2)
        checkList().findingItems(driver=driver, startIndex=startItemOnPage)
        if startItem <=100:
            for page in range(startOnPage, lengthPages):
                driver.find_elements(By.CSS_SELECTOR, locators.forPageLength)[page].click()
                time.sleep(2)
                checkList().findingItems(driver=driver, startIndex=0)
        else:
            for page in range(startOnPage + 1, lengthPages):
                driver.find_elements(By.CSS_SELECTOR, locators.forPageLength)[page].click()
                time.sleep(2)
                checkList().findingItems(driver=driver, startIndex=0)


class tryToBid():

    def clickOnBid(self, wait, driver):

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
            driver.find_element(By.CSS_SELECTOR, '#vi_oly_powerBid > div > div.clz > div > div').click()
            print('modal za poboljsanje ponude se pojavio')
            print('f')
        except:
            print('modal za poboljsanje ponude nije se pojavio')
            pass