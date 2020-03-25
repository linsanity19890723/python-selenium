from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')

LoginUrl = ('https://stg.e-pai-ke.com/login?back=http%3A%2F%2Fstg.e-pai-ke.com')
UserName = ('linsanity19890721@gmail.com')
UserPass = ('a94rup450')

driver.get(LoginUrl)
driver.find_element_by_id('email').send_keys(UserName)
driver.find_element_by_id('password').send_keys(UserPass)
driver.find_element_by_id('password').send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_xpath("//a[@class='itemthumb']//img").click()
time.sleep(3)
driver.find_element_by_xpath("//div[@class='side on']//li[1]//a[1]").click()
time.sleep(3)
driver.find_element_by_xpath("//a[@class='cancelBtn']//em").click()
time.sleep(3)
driver.find_element_by_xpath("//a[@id='delOK']").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@class='modal-body']//a[@class='close']").click()