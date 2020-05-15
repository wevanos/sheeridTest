from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from chromedriver_py import binary_path

#CONST

#LOCATORS
emailInput = (By.ID,"login-email")
passInput = (By.ID,"login-password")
loginSubmit = (By.XPATH,"//button[@data-analytics='sign-in-btn']")

createVProgram = (By.CSS_SELECTOR,"._2dnELS7tE881mbvHYoZ5CR ")
militaryTile = (By.XPATH,"//div[@data-analytics='program-editor-credentials-list-tile-military-trial-v2']")
nextFButton = (By.XPATH,"//button[@data-analytics='customizeForm Next']")
nextTButton = (By.XPATH,"//button[@data-analytics='customizeTheme Next']")
nextOButton = (By.XPATH,"//button[@data-analytics='chooseOffer Next']")
saveButton = (By.XPATH,"//button[@data-analytics='finish Save']")

createdProgram = (By.ID,"5ebeb561612e7e1ac35466d7")
openForom = (By.XPATH,"//button[@data-analytics='install-demo-link']")

driver = webdriver.Chrome(executable_path=binary_path)
driver.get(URL)

def waitElement(element):
    return WebDriverWait(driver,10).until(EC.visibility_of_element_located(element))

def clickElement(element):
    element = waitElement(element)
    element.click()

def setElementText(element,text):
    element = waitElement(element)
    element.send_keys(text)

#STEPS
setElementText(emailInput,USER)
setElementText(passInput,PASS)
clickElement(loginSubmit)

clickElement(createVProgram)
clickElement(militaryTile)
clickElement(nextFButton)
clickElement(nextTButton)
clickElement(nextOButton)
clickElement(saveButton)

clickElement(createdProgram)
clickElement(openForom)

driver.close()
driver.quit()