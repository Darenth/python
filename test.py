from selenium import webdriver
import  selenium
from  selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

driver = webdriver.Firefox(executable_path='D:\Code\Selenium\geckodriver.exe')
driver.implicitly_wait(10)
driver.get('https://selenium.dev/') #link to go
elem=driver.find_element_by_link_text("Downloads")
print(elem.get_attribute('href'))


def Synthema():
    driver.find_element_by_id("story").send_keys("Rammstein")
    wait = WebDriverWait(driver, 10)
    a=driver.find_element_by_id("auth")
    if(driver.find_element_by_id("auth")):
        first_result =wait.until(presence_of_element_located((By.ID,"auth")))
        driver.find_element_by_id("auth").click()
        driver.find_element_by_name("login_name").send_keys("lomicki")
        driver.find_element_by_name("login_password").send_keys("lomicki")
        driver.find_element_by_class_name("bbcodes").click()
        search_field = driver.find_element_by_id("story")
        search_field.send_keys("Rammstein")
        search_field.send_keys(Keys.ENTER)


#WebDriverWait(driver,10).until(EC.title_is("Wikipedia"))
#search_button=driver.find_element_by_xpath("/html/body/div[2]/form/fieldset/button")
#search_button.click()
# assert "Test automation" in driver.title
# #assert "es automation" in driver.page_source
# driver.quit()


# def driver(request):
#     wd=webdriver.Firefox(executable_path='D:\Code\Selenium\geckodriver.exe')
#     request.addfinalizer(wd.quit)
#     return  wd
#
# def test_example(driver):
#     driver.get("https://www.google.com/")
#     driver.finde_element_by_name("q").send_keys("wedriver")
#
#
# driver()
# test_example()
