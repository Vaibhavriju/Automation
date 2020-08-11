from selenium import webdriver
browser=webdriver.Chrome(r"C:\Users\vaibh\chromedriver")
browser.get("https://www.primevideo.com/detail/0OSEWAWFH8U83BJON2GV8UJQPP/ref=atv_sr_def_c_unkc__1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B0863KQBJ7&qid=1587984539")
elem=browser.find_element_by_link_text("Sign In")
elem.click()form 

search=browser.find_element_by_id("ap_email")

search.send_keys("vaibhavrijumishra@gmail.com")
