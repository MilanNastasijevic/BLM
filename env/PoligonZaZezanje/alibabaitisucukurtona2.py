from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from methodsCorrection import *


driver = webdriver.Chrome('/Users/milannastasijevic/Desktop/testScripts/BLM/webdrivers/chrome/chromedriver')
itemsPerPage=25 #it could be 25,50,100,200 , not finished with this. Put it in current url
driver.get('https://www.ebay.com/sch/gooditem6699/m.html?_nkw=&_armrs=1&_ipg=&_from=&rt=nc&LH_Auction=1&_ipg='+str(itemsPerPage))
driver.set_window_size(1440,900)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'#gh-ug > a').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'#userid').send_keys('sanda86posao@gmail.com')
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'#pass').send_keys('Flower08091986')
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR,'#sgnBt').click()
# driver.find_element(By.CSS_SELECTOR,'#DashSortByContainer > ul.sel > li > div > a').click()
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,'#SortMenu > li:nth-child(3) > a').click()
time.sleep(2)
items = driver.find_elements(By.CSS_SELECTOR,'li.sresult.lvresult.clearfix.li h3.lvtitle')
# items = driver.find_elements(By.CSS_SELECTOR,'ul#ListViewInner h3 a')
currentURL = driver.current_url
print(currentURL)
newURL=currentURL+'&_ipg='+str(itemsPerPage)
print(newURL)
driver.get(newURL)
duzina_liste_itema = len(items)
print(duzina_liste_itema)
wait = WebDriverWait(driver, 10)
startItem = 0

pageForMethods().additionalMethod(startItem=startItem, driver=driver)
# pageMethods().trasferThroughPages(driver=driver)

# checkList().findingItems(driver=driver,startIndex=startItem)
# pageSol(duzina_liste_itema=duzina_liste_itema, driver=driver, wait=wait, n=startItem)

# for i in range(3, duzina_liste_itema):
#     print(i)
#     time.sleep(15)
#     element = driver.find_elements(By.CSS_SELECTOR, 'ul#ListViewInner h3 a')[i].click()
#
#     element1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#MaxBidId')))
#     time.sleep(2)
#     driver.find_element(By.CSS_SELECTOR,'#MaxBidId').send_keys('0.3')
#     time.sleep(3)
#     driver.find_element(By.CSS_SELECTOR,'#bidBtn_btn').click()
#     time.sleep(2)
#     try:
#         driver.find_element(By.CSS_SELECTOR,'#w1-28-_reviewBidSec_btn').click()
#     except:
#         pass
#     try:
#         driver.find_element(By.CSS_SELECTOR,'#w1-29-_reviewBidSec_btn').click()
#     except:
#         pass
#     try:
#         driver.find_element(By.CSS_SELECTOR,'#w1-30-_reviewBidSec_btn').click()
#     except:
#         pass
#     time.sleep(15)
#     try:
#         driver.find_element(By.CSS_SELECTOR,'#vi_oly_powerBid > div > div.clz > div > div').click()
#     except:
#         pass
#     try:
#         print('usao sam u novododati try except block')
#         driver.execute_script('$("div[class="clzBtn"]).click()')
#         driver.execute_script('document.querySelector("#smtBackToAnchor").click()')
#     except:
#         print('izasao sam u novododati try except block')
#         pass
#     time.sleep(3)
#     driver.back()
#     time.sleep(2)
#     # driver.back()
#     # time.sleep(3)
#     # driver.back()
#     # time.sleep(5)
