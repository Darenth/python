
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import  Select

driver = webdriver.Firefox(executable_path='D:\Code\Selenium\geckodriver.exe')

driver.get('https://www.formstack.com/templates/online-event-registration?utm_source=eventregistrationforms&utm_medium=referral&utm_campaign=leadgen')
driver.find_element_by_xpath('/html/body/section[1]/div[2]/div[1]/a[2]').click()
element=driver.find_element_by_id('field43254047')
drp=Select(element)
drp.select_by_visible_text('3')
