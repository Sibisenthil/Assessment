from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.officeholidays.com/countries/india/2021")
driver.implicitly_wait(2)
table=driver.find_element(By.XPATH, "//table[contains(@class,'country-table')]")
print(table)

