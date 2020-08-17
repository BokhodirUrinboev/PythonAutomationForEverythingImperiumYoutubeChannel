from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
seul = driver.find_element_by_xpath('//*[@id="box5"]')
korea = driver.find_element_by_xpath('//*[@id="box105"]')
actions = ActionChains(driver)
actions.drag_and_drop(seul, korea).perform()