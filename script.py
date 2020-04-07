from bs4 import BeautifulSoup as BS
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException      
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

#URL from which I start
URL = 'https://www.imdb.com/title/tt1856010/episodes?season=1&ref_=tt_eps_sn_1'

#Setting up the driver and executing Chrome using chromedriver.exe
driver = webdriver.Chrome(executable_path='chromedriver')
#Openning website saved in URL variable
driver.get(URL)

#Function to check if element exists on webpage
def checkIfElementExists(id):
	try:
		driver.find_element_by_id(id)
	except NoSuchElementException:
		return False
	return True

#Function to scrape average rating from each episode in series
def getRatingOfSeries():
	all_ratings = []
	for number in range(1,30):
		try:
			rating = driver.find_element_by_xpath("//*[@id='episodes_content']/div[2]/div[2]/div[{num}]/div[2]/div[2]/div[1]/span[2]".format(num = number))
			all_ratings.append(rating.text)
		except:
			print ("ERR")
			break
	return all_ratings

#Finding the button to switch to the next episode
nextSer = driver.find_element_by_xpath("//*[@id='load_next_episodes']")
#List to store ratings
ratings = []

#Appending ratings for each episode from series to ratings list
ratings.append(getRatingOfSeries())

#Switching to next series
nextSer.click()

#Waiting for page to load
time.sleep(2)

#Appending ratings for each episode from series to ratings list
ratings.append(getRatingOfSeries())

#Printing out the results
print (ratings)