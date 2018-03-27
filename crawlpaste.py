from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib import urlopen
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




def Extractlinks(driver,keywords):
	driver.get('https://pastebin.com')
	search_bar = driver.find_element_by_xpath('//*[@id="cse-search-box"]/input')
	search_bar.send_keys(keywords)
	#onclick = driver.find_element_by_xpath('//*[@id="res"]/tbody/tr/td[4]/form/button')
	search_bar.send_keys(Keys.RETURN)
	pastes = []
	xpath = '//*[@id="___gcse_0"]/div/div/div/div[5]/div[2]/div/div/div[3]/div[{}]/div[1]/div[1]/div/a'
	for i in range(1, 4):
		str_xpath = xpath.format(str(i))
		url_element = driver.find_element_by_xpath(str_xpath)
		pastes.append(url_element.get_attribute("href"))
	return pastes

	

def getdriver(chromedriver):
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	options.add_argument('--ignore-certificate-errors')
	options.add_argument('disable-gpu')
	options.add_argument('window-size=1200,1100')
	driver= webdriver.Chrome(chromedriver,chrome_options=options)
	return driver


def crawllinks(driver,leaklinks):
	for link in leaklinks:
		driver.get(link)
		data = driver.find_element_by_xpath('//*[@id="code_buttons"]/span[1]/a[2]')
		data.send_keys(Keys.RETURN)

		

if __name__ == "__main__":
	keywords = str(raw_input("enter keywords"))
	chromedriver = '/home/hanlak/Music/chromedriver'
	print "assining driver.."
	driver = getdriver(chromedriver)
	print "driver assigned and exctracting links"
	leaklinks = Extractlinks(driver,keywords)
	print "download in progress............"
	crawllinks(driver,leaklinks)
	print "Download completed thankyou"
