from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\\Users\\Hemanth Naidu\\chromedriver_win32\\chromedriver.exe")'''
driver.get("https://www.milonic.com/login.php")
driver.find_element_by_name("email").send_keys("mail2hemanthsurya@gmail.com")
driver.find_element_by_name("password").send_keys("7382956781")
driver.find_element_by_name("logcount").click()'''

driver.get("https://www.excellbroadband.com/billpay.html")
driver.find_element_by_css_selector("#customerid").send_keys("89980")
driver.find_element_by_css_selector("#phone").send_keys("7382956781")
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome(executable_path="C:\\Users\\Hemanth Naidu\\chromedriver_win32\\chromedriver.exe")
#code to get connect to web application on which a test script is written

driver.get("https://www.globalsqa.com/samplepagetest")
#code to select tag in the above mensioned webapplication
dropdown=Select(driver.find_element_by_id("g2599-experienceinyears"))
#dropdown.select_by_index(3)
dropdown.select_by_visible_text("10+")'''

'''from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\\Users\\Hemanth Naidu\\chromedriver_win32\\chromedriver.exe")'''

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.globalsqa.com/samplepagetest")
#write a code find all checkboxes at time,go with xpath
checkboxes=driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))
for i in checkboxes:
    i.click()
#write