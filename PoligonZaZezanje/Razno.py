import os
from datetime import datetime
import selenium.webdriver

class a():
    def browserStarting(driver):
        driver = selenium.webdriver.Firefox()

class b():
    def directoryCreationMethod(self):
        newpath = r'C:\Users\milan.nastasijevic.MOZZART\Desktop\TestsReports'

        if not os.path.exists(newpath):
            os.makedirs(newpath)
        else:
            print 'folder creation failed'

        trenutnoVreme = datetime.now().strftime('%Y-%m-%d %H:%M:%S').replace(':','.')
        TextFile = open(os.path.join(newpath,'Test Creation Of Lotto Ticket' + trenutnoVreme) + '.txt' ,'w')

class c():
    def firefoxMaximizeWindowsMethod(self):
        try:
            selenium.webdriver.Firefox().maximize_window()
            print ('for firefox starting')
        except:
            print ('overide firefox trouble with maximazing browser window')

