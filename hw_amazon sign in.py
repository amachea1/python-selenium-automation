from selenium import webdriver
from selenium.webdriver.common.by import By


# init driver
driver = webdriver.Chrome(executable_path=r"C:\Users\17132\Documents\careerist_automation\python-selenium-automation\chromedriver.exe")
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# click orders
driver.find_element(By.XPATH, "//span[text()='& Orders']").click()

# verify sign in page
sign_in=driver.find_element(By.XPATH,"//h1[@class='a-spacing-small']" )

print(sign_in.is_displayed())

email_input=driver.find_element(By.ID,"ap_email")

print(email_input.is_displayed())

print('test case passed')

driver.quit()


