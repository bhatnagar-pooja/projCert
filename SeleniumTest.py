from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome("C:\Users\pooja_000\PycharmProjects\javatry\driver\chromedriver.exe")
driver.set_page_load_timeout(100)

driver.get("http://35.223.44.160:32768")
driver.find_element_by_xpath("/html/body/div/header/nav/a[2]").click()

try:
    a = driver.find_element_by_xpath("/html/body/p[1]");
    if a.is_displayed():
        print("Success")

except NoSuchElementException:
      print ("Fail")

driver.quit()
