import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import mysql.connector
from selenium.webdriver.chrome.options import Options

# Configurer les options pour Chrome en mode headless

conn = mysql.connector.connect(
	user='root',
	host='localhost',
	database='fittracker',
	passwd='omar123Lecor'
)
cursor = conn.cursor()
cursor = conn.cursor(buffered=True)

def userfd(usernmae,time,foodname,foodingredient,servingn):
	chrome_options = Options()
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--disable-gpu")
	chrome_options.add_argument("--no-sandbox")

	service = Service(executable_path='chromedriver.exe')
	driver = webdriver.Chrome(service=service,options=chrome_options)
	driver.get("https://happyforks.com/analyzer")
	input_element = driver.find_element(By.ID, "recipe-text")
	input_element.send_keys(foodingredient)
	servin_num = driver.find_element(By.ID, "recipe-servings")
	servin_num.clear()
	servin_num.send_keys(servingn)
	search = driver.find_element(By.XPATH, "//button[@class='gfx gfx-lock']/span")
	search.click()
	WebDriverWait(driver, 5).until(
		ec.presence_of_element_located((By.XPATH, "//span[@class='label']/span[not(@class)]"))
	)
	data = driver.find_elements(By.XPATH, "//span[@class='label' or @class='label cols-2']/span[not(@class)]")
	liste = []
	for don in data:
		liste.append(don.text)
	cursor.execute("insert into foodcont values(%s,%s,%s,%s,%s,%s,%s)",[usernmae,time,foodname,float(liste[0]),float(liste[1]),float(liste[3]),float(liste[2])])
	conn.commit()
	driver.quit()