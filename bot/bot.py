#!/usr/bin/python3
#This bot simulate a victim logged in his bank account and click on malicious link

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time, re, sys
import pymysql.cursors

username = "admin"
password = "1RIKHCNOPORksIqVHmSxuR762uFX8JwF"
url = "http://flaskapp:5000/BankLogin"
# url = "http://172.20.0.3:5000/BankLogin"
inbox = "http://flaskapp:5000/BankInboxRequests"
searchProfile = "http://flaskapp:5000/BankSearchUser"

URL_PATTERN = r'(http[s]?://[^\s]+)'



if __name__ == "__main__":

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--mute-audio')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--disable-infobars')
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--no-sandbox')
    options.add_argument('--no-zygote')
    options.add_argument('--log-level=3')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--disable-web-security')
    options.add_argument('--disable-features=VizDisplayCompositor')
    options.add_argument('--disable-breakpad')
    options.set_capability("acceptInsecureCerts", True)
    
    desired_capabilities = options.to_capabilities()
    desired_capabilities['acceptInsecureCerts'] = True
   
    #bot = webdriver.Chrome("./chromedriver")

    bot = webdriver.Chrome(
        options=options,
        desired_capabilities=desired_capabilities
    )


    # try to connect
    while True:
        try:
            print("try to connect with app")
            bot.get(url)
            break
        except Exception as e:
            print(e, file=sys.stderr)
            print("app not ready")
            time.sleep(3)

    #login
    bot.find_element("id", "username").send_keys(username)
    bot.find_element("id", "password").send_keys(password)
    bot.find_element(By.CLASS_NAME, "login-button").click()
    bot.get(inbox)

    #read messagges and do stuff
    while True:
        time.sleep(5)
        bot.refresh()
        object_messagges = bot.find_elements(By.CSS_SELECTOR, "text")
        object_users = bot.find_elements(By.CSS_SELECTOR, "strong")
        
        users = []
        messagges = []

        for obj_usr, obj_msg in zip(object_users, object_messagges):
            
            users.append(obj_usr.text.strip().replace(':',''))
            messagges.append(obj_msg.text)
            
        print(users)
        print(messagges)
        for user, message in zip(users,messagges):
            
            url = re.findall(URL_PATTERN, message) #cerca url nel messaggio
            
            if(len(url) != 0): #se ci sono url
                try:
                    bot.get(url[0]) #vai al primo url
                    time.sleep(5)
                except Exception as e:
                    print(e)
            else:
                bot.get(searchProfile)
                bot.find_element(By.NAME, "user").send_keys(user)
                bot.find_element(By.NAME, "search").click()
                time.sleep(5)

            bankconnection = pymysql.connect(host='db',
                                 user='bankadmin',
                                 password='SuperAdminPassword!',
                                 database='banksystem',
                                 cursorclass=pymysql.cursors.DictCursor)
            try:
                with bankconnection.cursor() as cursor:
                        print("try to delete %s" %message) 
                        cursor.execute("UPDATE accounts SET description = 'None' WHERE username = '%s'" %user)
                        cursor.execute("DELETE from messages where text = '%s'" %message)
                        bankconnection.commit()
            except Exception as e:
                print(e)

        bot.get(inbox)    



