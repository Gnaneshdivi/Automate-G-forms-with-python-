from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import date

today = date.today()
formurl='' ##form url
dat=today.strftime("%d/%m/%Y")
print(dat)

web= webdriver.Chrome(ChromeDriverManager().install())
web.get(formurl)


nameid=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
nameid.send_keys({testername})
time.sleep(1)  ##Name

manid=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
manid.send_keys({Email})
time.sleep(1) ##Email

testid=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
testid.send_keys({testcase})
time.sleep(1) ##Address

dateid=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/textarea')
dateid.send_keys({dat})
time.sleep(1) ##Phone number



macid=web.find_element_by_xpath('//*[@id="i5"]/div[3]/div')
macid.click()  ##Radio Button 

macid=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
macid.click()  ##submit Button 




















