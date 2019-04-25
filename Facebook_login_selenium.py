from selenium import webdriver 
from time import sleep 

user='Your Email address here'
password='Your Password here' 

driver = webdriver.Chrome('path to your Chromedriver here')
driver.get('https://www.facebook.com/')
print ("Opened facebook")
sleep(2)

username_box = driver.find_element_by_id('email') 
username_box.send_keys(user) 
print ("Email Id entered") 
sleep(2) 

password_box = driver.find_element_by_id('pass') 
password_box.send_keys(password) 
print ("Password entered") 

login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 

print ("Done") 
print("Finished") 
