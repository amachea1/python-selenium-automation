from selenium import webdriver
from selenium.webdriver.common.by import By


# init driver
driver = webdriver.Chrome(executable_path=r"C:\Users\17132\Documents\careerist_automation\python-selenium-automation\chromedriver.exe")
driver.maximize_window()

driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('bucket hat')

driver.find_element(By.ID,'nav-search-submit-button').click()

expected_result='"bucket hat"'
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

assert expected_result == actual_result

print('test case passed')

driver.quit()



