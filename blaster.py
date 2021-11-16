from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import random
import json

import time
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

from dbConnect import connect

def human_text(text, elem, driver):
    for character in text:
        actions = ActionChains(driver)
        actions.move_to_element(elem)
        actions.click()
        actions.send_keys(character)
        actions.perform()
        time.sleep(random.uniform(0.0001,0.002))

def blasterFunc(username, password, credentials, message, message2, message3, message4):
    print("getting to start")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
   
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("user-data-dir=/tmp/tarun")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430 Safari/537.36")

   
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options) 

    print("b4 link")

    
    driver.implicitly_wait(30)
    print("routing to login link")
    driver.get('https://www.instagram.com/direct/inbox/')
    print('success')
    time.sleep(5)
    print(driver.current_url)
   
    if '/accounts/login/' in driver.current_url:
        #Loggging into the app and closing all other popups that may appear on login
        element = driver.find_element_by_name('username')
        human_text(username, element, driver)
        element = driver.find_element_by_name('password')
        human_text(password, element, driver)

        element = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

        time.sleep(4)
        print("logged in")
        db = connect("MessageBlaster")
        
        if 'two_factor' in driver.current_url:

           
                securityCode = "!"
                while securityCode == "!":
                    print("Waiting for code....")
                    try:
                        cursor = db.SecurityCode.find_one({"userName":username})
                        securityCode = cursor["securityCode"]
                        
                    except:
                        securityCode == "!"
                    time.sleep(1)
                try:
                    print("Security Code is:"+str(securityCode))
                    element = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[1]/div/label/input').send_keys(securityCode)
                   
                    time.sleep(4)
                    element = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[2]/button').click()
                    time.sleep(10)
                except Exception as e:
                    print(e)
        
        else:
            print("No Need to get Security code")
        time.sleep(3)
    else:
        print("No need to login!")



    #Code-block to send out messages

   
    print("xxxxxxxx")
    print(driver.current_url)
    print("xxxxxxx")


    time.sleep(5)
    qqq = 0
    print(credentials[0])
    for x in credentials:
        
        print(x)
       
        messageFormat = message.format_map(x)
        messageFormat1 = message2.format_map(x)
        messageFormat2 = message3.format_map(x)
        messageFormat3 = message4.format_map(x)
       
      
       
        element = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
        time.sleep(2)
          

        time.sleep(2)
       

       
        element = driver.find_element_by_class_name("j_2Hd.uMkC7.M5V28")
       
       
        time.sleep(2)
        human_text(x["username"], element, driver)
        time.sleep(7)
        element = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]/div[1]/div/div[3]/button').click()
       
        time.sleep(2)
        element = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/div/button').click()
        time.sleep(2)
        #Section where message block is sent
        
        element = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(messageFormat)
        
        #These sections are needed if we want to send messsages in different paragraphs(all in the same message)
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        element = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(messageFormat1)
        
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        element = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(messageFormat2)
        
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        element = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(messageFormat3)
        
        time.sleep(2)
        element = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()



    driver.quit()
