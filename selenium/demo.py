from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://www.google.com')
# driver.get('http://www.wikipedia.org')

# Refresh the page
# time.sleep(15)
# driver.refresh()

# Finding element by its name
# elem = driver.find_element_by_name('q')

# By.XPATH method
# elem = driver.find_element(By.XPATH,'//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')

# Find element by link text
# elem = driver.find_element_by_link_text('Advertising')
# elem.click()
# time.sleep(5)
# elem = driver.find_element_by_link_text('Cost')
# time.sleep(5)
# elem.click()

# back/forward button
# elem = driver.find_element_by_link_text('About')
# time.sleep(5)
# driver.back()
# time.sleep(5)
# driver.forward()


# time.sleep(5)
# elem.clear()
# elem.send_keys("Python")
# elem.send_keys(Keys.RETURN)

# Scrolling **Wikipedia, not google site***
# elem = driver.find_element_by_tag_name('html')
# elem.send_keys(Keys.END)
# time.sleep(5)
# elem.send_keys(Keys.HOME)

# Finding page url
elem = driver.find_element_by_link_text('About')
time.sleep(5)
elem.click()
time.sleep(5)
print (driver.current_url)
