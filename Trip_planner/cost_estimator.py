from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# city - iataCode

class EstimatedCost:
    def __init__(self, city):
        self.driver = webdriver.Chrome(executable_path="C:\Development\chromedriver.exe")
        self.hotel_per_night_cost = 0
        self.city = city
        self.hotel_cost()
    def hotel_cost(self):
        self.driver.get("https://www.agoda.com/en-in/")
        sleep(1)
        input = self.driver.find_element_by_xpath('//*[@id="SearchBoxContainer"]/div[1]/div/div[2]/div/div/div[2]/div/div/input')
        input.send_keys(self.city)
        sleep(2)
        input.send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath('//*[@id="SearchBoxContainer"]/div[2]/button/div').click()
        self.hotel_per_night_cost = self.driver.find_element_by_class_name("PropertyCardPrice__Value").text
        self.hotel_per_night_cost =+ int(''.join(self.hotel_per_night_cost.split(",")))



# c =EstimatedCost('BER').hotel_cost()