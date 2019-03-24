from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class WorkingWithElementsList():

    def testListOfElements(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        try:
            driver.maximize_window()
            print ('for firefox starting')
        except:
            print ('overide firefox trouble with maximazing browser window')
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        radioButtonsList = driver.find_elements(
            By.XPATH, "//input[contains(@type,'radio') and contains(@name,'cars')]")
        size = len(radioButtonsList)
        print("Size of the list: " + str(size))

        for radioButton in radioButtonsList:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(2)

ff = WorkingWithElementsList()
ff.testListOfElements()