
import os
import time
import sys
from datetime import datetime, date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
error = (NoSuchElementException, ElementNotInteractableException)
browser = webdriver.Firefox(executable_path=r'C:\Users\garren-james\AppData\Local\geckodriver')
browser.get('http://ns-dcf-wvtws01/Default.aspx?tab=1')
loc = (r'C:\Users\garren-james\ProdverLogs')
fileName = 'prodver_log_' + str(date.today()) + '.txt'
path = loc + "\\" +fileName
user = loc + "\\ADICred.txt"
signin = open(user, 'r')
user = signin.read().splitlines()
htmlElem = browser.find_element_by_id('ctl07_tbUsername')
htmlElem.send_keys(user[0])
htmlElem = browser.find_element_by_id('ctl07_tbPassword')
htmlElem.send_keys(user[1])
htmlElem = browser.find_element_by_id('ctl07_lbSubmit')
htmlElem.click()
try:
    htmlElem = browser.find_element_by_id('ucMenu_lblPsnDocSearch')
    log = open(path, "w+")
    log.write('Log In Test: Passed\n')
    log.close()
except:
    log = open(path, "w+")
    log.write('Log In Test: Failed\n')
    log.close()
    sys.exit('No sign on available!')


htmlElem = browser.find_element_by_id('ucMenu_lblPsnDocSearch')
htmlElem.click()
htmlElem = browser.find_element_by_id('ctl07_ITLastName')
htmlElem.send_keys(user[2])
htmlElem = browser.find_element_by_id('ctl07_ITFirstName')
htmlElem.send_keys(user[3])
htmlElem = browser.find_element_by_id('ctl07_BTNSearch')
htmlElem.click()
try:
    htmlElem = browser.find_element_by_id('ctl07_grdView_HLKDocNumber_0')
    log = open(path, "a")
    log.write('Person Search Test: Passed\n')
    log.close()
except:
    log = open(path, "a")
    log.write('Person Search Test: Failed\n')
    log.close()


htmlElem = browser.find_element_by_id('ucMenu_lblDocSearch')
htmlElem.click()
select = Select(browser.find_element_by_id('ctl07_ddlRegion'))
select.select_by_value('99')
select = Select(browser.find_element_by_id('ctl07_ddlWorkGroupType'))
select.select_by_value('12454')
select = Select(browser.find_element_by_id('ctl07_ddlWorkGroup'))
select.select_by_value('17883')
htmlElem = browser.find_element_by_id('ctl07_lbSubmit')
htmlElem.click()
try:
    htmlElem = browser.find_element_by_id('ctl07_ucSearchResults_dgSearchResults_hlThumb_0')
    log = open(path, "a")
    log.write('Workgroup Search Test: Passed\n')
    log.close()
except:
    log = open(path, "a")
    log.write('Workgroup Search Test: Failed\n')
    log.close()


htmlElem = browser.find_element_by_id('ctl07_ucSearchResults_dgSearchResults_lblDocumentNumber_0')
docNum = htmlElem.text
htmlElem = browser.find_element_by_id('ucMenu_lblPsnDocSearch')
htmlElem.click()
htmlElem = browser.find_element_by_id('ctl07_ITDocNumber')
htmlElem.send_keys(docNum)
htmlElem = browser.find_element_by_id('ctl07_BTNSearch')
htmlElem.click()
htmlElem = browser.find_element_by_id('ctl07_grdView_lbReIndex_0')
htmlElem.click()
htmlElem = browser.find_element_by_id('ctl07_txtCaseID')
htmlElem.send_keys(user[4])
htmlElem = browser.find_element_by_id('ctl07_btnSearch')
htmlElem.click()
try:
    htmlElem = browser.find_element_by_id('ctl07_grdPersonList_rdbUser_0')
    log = open(path, "a")
    log.write('Index FLODS Search Test: Passed\n')
    log.close()
except:
    log = open(path, "a")
    log.write('Index FLODS Search Test: Failed\n')
    log.close()


htmlElem = browser.find_element_by_id('ctl07_grdPersonList_rdbUser_0')
htmlElem.click()
select = Select(browser.find_element_by_id('ctl07_IDDLDocType'))
select.select_by_value('5')
select = Select(browser.find_element_by_id('ctl07_LBSubType'))
select.select_by_value('1350')
htmlElem = browser.find_element_by_id('ctl07_btnContinue')
htmlElem.click()
htmlElem = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.ID, 'ctl07_btnSaveAndContinue')))
try:
    htmlElem = browser.find_element_by_id('ctl07_btnSaveAndContinue').is_enabled()
    if htmlElem == True:
        log = open(path, "a")
        log.write('Index Test: Passed\n')
        log.close()
    else:
        log = open(path, "a")
        log.write('Index Test: Failed\n')
        log.close()
except:
    log = open(path, "a")
    log.write('Index Test: Failed\n')
    log.close()


htmlElem = browser.find_element_by_id('ctl07_btnCancell')
htmlElem.click()
htmlElem = browser.find_element_by_id('ucMenu_lblPsnDocSearch')
htmlElem.click()
htmlElem = browser.find_element_by_id('ctl07_ITDocNumber')
htmlElem.send_keys(user[5])
htmlElem = browser.find_element_by_id('ctl07_BTNSearch')
htmlElem.click()
htmlElem = browser.find_element_by_id('ctl07_grdView_HLKDocNumber_0')
htmlElem.click()
time.sleep(20)
browser.switch_to.window(browser.window_handles[1])
try:
    htmlElem = browser.find_element_by_id('ErrorMessage')
    log = open(path, "a")
    log.write('Document available Test: Failed\n')
    log.close()
    browser.close()
except:
    log = open(path, "a")
    log.write('Document Available Test: Passed\n')
    log.close()
    browser.close()


browser.switch_to.window(browser.window_handles[0])
htmlElem = browser.find_element_by_id('ucMenu_lblAvailability')
htmlElem.click()
timeout = 60   # 5 minutes from now
timeout_start = time.time()
while time.time() < timeout_start + timeout:
    time.sleep(1)
    htmlElem = browser.find_element_by_id('ucMenu_lblInbox')
    htmlElem.click()
    test = 0
    print(time.time())
    if test == 5:
        break
    test = test - 1


try:
    htmlElem = browser.find_element_by_id('ctl07_dgInboxList_lblSubject_0')
    log = open(path, "a")
    log.write('WLM Test: Passed\n')
    log.close()
    htmlElem = browser.find_element_by_id('ucMenu_lblAvailability')
    htmlElem.click()
except:
    log = open(path, "a")
    log.write('Index Test: Failed\n')
    log.close()
    htmlElem = browser.find_element_by_id('ucMenu_lblAvailability')
    htmlElem.click()


browser.quit()
