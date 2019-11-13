######### AUTHOR : RAJ PRASAD KUIRI #########

from selenium import webdriver
driver=webdriver.Chrome(executable_path="G:\\webdriver\\chromedriver.exe")
driver.get("http://www.instagram.com")
driver.save_screenshot("D:\\c\\Automate Testing")
print("screen shot capture")