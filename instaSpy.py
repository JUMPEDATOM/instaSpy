from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import pandas as pd
import time
import random
import os

baseUrl = 'https://www.instagram.com/'

### Load From Env File If Exist ###
load_dotenv()

### WebDriver Setting ###
options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--incognito")
options.binary_location = os.environ['BROWSER_PATH']

driver = webdriver.Chrome(executable_path= os.environ['DRIVER_PATH'], chrome_options= options)
driver.maximize_window()

def authentication(url, userName, passWord):
    print("[Info] - Logging in...")
    #open Selected URL
    driver.get(url)
    time.sleep(random.randrange(5,10))
    
    #Check For Cookies
    try:
        cookiesButton = driver.find_element(By.XPATH, "//button[@class='_a9-- _a9_0']")
        cookiesButton.click()

    except NoSuchElementException:
        print("[Info] - Instagram did not require to accept cookies this time.")

    #Fill-In Coordinates
    user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
    user.send_keys(userName)
    time.sleep(random.randrange(2,4))

    key = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
    key.send_keys(passWord)
    time.sleep(random.randrange(2,4))

    loginButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')))
    loginButton.click()
    time.sleep(random.randrange(5,10))

    #If Logged-In Account Has two-step Verification
    try:
        if driver.current_url == 'https://www.instagram.com/accounts/login/two_factor?next=%2F':
            code = input("[Info] - Enter 2-Step Verification Code: ")
            securityCode = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'verificationCode')))
            securityCode.send_keys(code)
            time.sleep(random.randrange(2,4))

            confirmButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Confirm']")))
            confirmButton.click()
            time.sleep(random.randrange(5,10))

    except:
        print("[Info] - Account does not have two-step verification")


def getUnfollowedList(url):
    print("[Info] - Collecting Data...")

    #Get Ride Of All Pop-Up
    firstNotNowButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@tabindex='0']")))
    firstNotNowButton.click()
    time.sleep(random.randrange(2,4))

    secondNotNowButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='_a9-- _a9_0']")))
    secondNotNowButton.click()
    time.sleep(random.randrange(4,6))

    #Direct To Profile Page
    driver.get(url + f"{os.environ['INSATGRAM_USERNAME']}/following")
    time.sleep(random.randrange(2,4))

    #Scroll in Following List
    scrollBox = driver.find_element(By.XPATH, "//div[@class='_aano']")
    lastHeight, currentHeight = 0, 1

    while lastHeight != currentHeight:
        lastHeight = currentHeight
        time.sleep(5)
        currentHeight = driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;", scrollBox)
    
    FollowingList = driver.find_elements(By.XPATH, "//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd']")
    following = []

    for user in FollowingList:
        href = user.get_attribute('href').split("/")[3]
        following.append(href)

    # print(following)
    
    driver.get(url + f"{os.environ['INSATGRAM_USERNAME']}/followers")
    time.sleep(random.randrange(4,6))

    scrollBox = driver.find_element(By.XPATH, "//div[@class='_aano']")
    lastHeight, currentHeight = 0, 1

    while lastHeight != currentHeight:
        lastHeight = currentHeight
        time.sleep(5)
        currentHeight = driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;", scrollBox)    

    FollowerList = driver.find_elements(By.XPATH, "//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd']")
    followers = []

    for user in FollowerList:
        href = user.get_attribute('href').split("/")[3]
        followers.append(href)

    # print(followers)

    unFollowers = []

    for element in following:
        if element not in followers:
            unFollowers.append(element)

    # print(unFollowers)


    #Insert To DataFrame
    print('[Info] - Saving...')
    followingDataFrame = pd.DataFrame(following,columns=["Usernames"])
    followingDataFrame.to_csv("Following.csv")

    followersDataFrame = pd.DataFrame(followers,columns=["Usernames"])
    followersDataFrame.to_csv("Followers.csv")

    unFollowersDataFrame=pd.DataFrame(unFollowers,columns=["Usernames"])
    unFollowersDataFrame.to_csv("unFollowers.csv")


    print("[DONE] - All Data Saved On CSV File!")


if __name__ == '__main__':
    authentication(baseUrl, os.environ['INSATGRAM_USERNAME'], os.environ['INSTAGRAM_PASSWORD'])
    getUnfollowedList(baseUrl)



