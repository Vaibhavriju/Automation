from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(r"C:\Users\vaibh\chromedriver")
driver.get("https://www.youtube.com/")
wait=WebDriverWait(driver,600)
#target='"Notice Board"'
string="The night we met"
#x_args='//span[contains(@title,'+ target +')]'
#target=wait.until(EC.presence_of_element_located((By.XPATH,x_args)))
#target.click() 
elem_1=driver.find_element_by_class_name("style-scope ytd-searchbox")
elem_1.send_keys(string+Keys.ENTER)
elem_2=driver.find_element_by_class_name("style-scope ytd-item-section-renderer")
elem_2.click()
