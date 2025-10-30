from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time 
import json
import requests
driver = webdriver.Chrome()


class GetInfo: 
    def __init__(self, login, password):
        self.login = login
        self.password = password
        
    def getGeneralUrl(self):
        login = self.login
        password = self.password
        
        driver.get("https://eduvulcan.pl/logowanie")

        wait = WebDriverWait(driver, 10)
        iframe = wait.until(EC.presence_of_element_located((By.ID, "respect-privacy-frame")))
        driver.switch_to.frame(iframe)

        accept_button = wait.until(EC.element_to_be_clickable((By.ID, "save-default-button")))
        accept_button.click()

        driver.switch_to.default_content()


        textBox = driver.find_element(by = By.CSS_SELECTOR, value="input")
        textBox.send_keys(login)

        next = driver.find_element(by = By.ID, value="btNext")
        next.click()




        password_box = wait.until(EC.element_to_be_clickable((By.ID, "Password")))

        password_box.send_keys(password)


        driver.find_element(by = By.ID, value="btLogOn").click()

        driver.implicitly_wait(2)


        link = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/a[1]")
        link.click()
        
        url = driver.current_url
        
        return url
    
    def getGrades(self):

            url = self.getGeneralUrl()
            
            driver.get(url)
            
        
            grades = driver.current_url

            change = grades.split("/")

            token = change[5]

            print(token)

            grades_url = f"https://uczen.eduvulcan.pl/tarnobrzeg/api/OcenyTablica?key={token}"

            driver.get(grades_url)

            grades = driver.find_element(By.XPATH, "/html/body").text
            
            return grades
        
login = "lockapo009@gmail.com"
password = "K@cper2009"

idk = GetInfo(login, password)

print (idk.getGrades())
            
