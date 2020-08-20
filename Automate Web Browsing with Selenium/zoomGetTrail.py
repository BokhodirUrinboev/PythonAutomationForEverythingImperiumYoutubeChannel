from selenium import webdriver
import pickle
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import string
from fake_useragent import UserAgent
OPTIONS = webdriver.ChromeOptions() 
OPTIONS.add_argument("--user-data-dir=C:\\Users\\Bokhodir\\AppData\\Local\\Google\\Chrome\\")
OPTIONS.add_argument("start-maximized")
OPTIONS.add_experimental_option("excludeSwitches", ["enable-automation"])
OPTIONS.add_experimental_option('useAutomationExtension', False)


class TempMail():
    def __init__(self):
        self.driver = webdriver.Chrome()

    # def generatedMail(self):
    #     letters = string.ascii_lowercase
    #     result_str = ''.join(random.choice(letters) for i in range(0,10))
    #     return result_str
    def getMail(self):
        self.driver.get('https://temp-mail.org/en/')
        sleep(20)
        inputMail = self.driver.find_element_by_xpath('//*[@id="mail"]')
        return inputMail.get_attribute('value')


class ZoomReg():
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options=OPTIONS)
        

    def assignDateOfBirth(self):
        self.driver.get('https://zoom.us/signup')
        sleep(5)
        day = self.driver.find_element_by_xpath('//*[@id="select-1"]')     
        month = self.driver.find_element_by_xpath('//*[@id="select-0"]')
        year = self.driver.find_element_by_xpath('//*[@id="select-2"]')
        assign_button = self.driver.find_element_by_xpath('//*[@id="age_gating_question"]/div/div[1]/button')
        day.click()
        sleep(1)
        day.send_keys("", Keys.ARROW_DOWN)
        day.send_keys("", Keys.ENTER)
        sleep(1)
        month.click()
        month.send_keys("", Keys.ARROW_DOWN)
        month.send_keys("", Keys.ENTER)
        sleep(1)
        year.click()
        for i in range(0,21):
            year.send_keys("", Keys.ARROW_DOWN)
            if i % 2 == 0:
                year.send_keys("", Keys.ENTER)
                
        for i in range(0,21):
            year.send_keys("", Keys.ARROW_DOWN)
            if i % 2 == 0:
                year.send_keys("", Keys.ENTER)
                
        sleep(1)
        assign_button.click()
        sleep(5)
    
    def registerMail(self, mail):
        # cookies = pickle.load(open("cookies.pkl", "rb"))
        # for cookie in cookies:
        #     self.driver.add_cookie(cookie)
        sleep(5)
        input = self.driver.find_element_by_xpath('//*[@id="email"]')
        button_register = self.driver.find_element_by_xpath('//*[@id="signup-form"]/div[3]/div/div[1]/a')
        input.send_keys(mail)
        sleep(5)
        button_register.click()
        sleep(60)
        # pickle.dump( self.driver.get_cookies() , open("cookies.pkl","wb"))


t = TempMail().getMail()
sleep(5)
z = ZoomReg()
z.assignDateOfBirth()
z.registerMail(t)