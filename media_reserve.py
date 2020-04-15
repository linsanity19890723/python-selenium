from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')

LoginUrl = ('https://stg.e-pai-ke.com/login?back=http%3A%2F%2Fstg.e-pai-ke.com')
UserName = ('$useraccount')
UserPass = ('$userpassword')

driver.get(LoginUrl)
driver.find_element_by_id('email').send_keys(UserName)
driver.find_element_by_id('password').send_keys(UserPass)
driver.find_element_by_id('password').send_keys(Keys.ENTER)
driver.save_screenshot('C:/Users/leo.lee/Desktop/暫存區/login.png')

driver.get("https://stg.e-pai-ke.com/search?sort=score")
driver.fullscreen_window()
time.sleep(3)
driver.find_element_by_xpath("//div[@class='rightBox']//div[1]//div[1]//div[3]//ul[1]//li[3]//a[1]//em[1]").click()
time.sleep(3)
driver.find_element_by_xpath("//a[contains(@class,'btn bookbtn showOrder')]").click()
time.sleep(3)
driver.find_element_by_xpath("//div[@class='select-wrapper iconsDate']//input[@class='select-dropdown']").click()
time.sleep(3)
driver.find_element_by_xpath("//div[@id='orderModal']//li[3]//span[1]").click()
time.sleep(3)
driver.find_element_by_xpath("//a[@id='orderOK']").click()
time.sleep(3)
driver.find_element_by_xpath("//a[@id='orderOK']").click()
time.sleep(2)
driver.close()
