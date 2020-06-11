from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import random
import names
from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys


POST_URL = "https://app.biorender.com/contest/profile/5dc321790d5929007dfbf7bb-satish-poojary/s-5ed39d568563ce00af3b4cc3-tumor-microenvironment-drives-cancer-progression"
SIGN_UP = "https://app.biorender.com/user/signup"


class User():
    f = names.get_first_name()
    l = names.get_last_name()
    n = random.randint(1, 10) * random.randint(200, 2000)


vote_count_needed = 1
# hello this is video!!

def vote():
    driver = webdriver.Chrome()
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.get(SIGN_UP)
    myUser = User()
    myUser.n *= random.randint(2, 10)
    sign_up_form = {'firstName': myUser.f, 'lastName': myUser.l,
                    'email': myUser.f + myUser.l + str(myUser.n) + '@gmail.com',
                    'password': 'password'}
    
    file1 = open("users.txt", "a")  # append mode
    file1.write(sign_up_form["email"])
    file1.close()
    
    print("user email is - ", sign_up_form["email"])
    driver.implicitly_wait(15)

    # sign up form iteration
    for key in sign_up_form:
        driver.find_element_by_name(key).send_keys(sign_up_form[key])

    driver.find_element_by_class_name(
        "user-form__main-button").send_keys(Keys.ENTER)

    driver.implicitly_wait(15)
    driver.find_element_by_xpath(
        "//button[@data-test='SIGNUP_ORGANIZATION_TYPE']").click()
    driver.implicitly_wait(1)
    driver.find_element_by_xpath(
        "//div[@data-test='dropdown-menu-item']").click()

    driver.find_element_by_xpath(
        '//button[@data-test="SIGNUP_ORGANIZATION_ROLE_FIELD"]').click()

    driver.implicitly_wait(15)
    driver.find_element_by_xpath(
        "//div[@data-test='dropdown-menu-item']").click()

    driver.find_element_by_name("organization").send_keys("DTU")
    # driver.find_elements_by_xpath("//input[@data-test='SIGNUP_LAB_NAME_FIELD'][1]").send_keys("NA")
    driver.get(POST_URL)
    driver.implicitly_wait(15)
    someList = driver.find_elements_by_xpath(
        "//button[@class='button vote-button__container outline contest-preview-modal__action']")
    for el in someList:
        el.click()
    time.sleep(3)
    driver.close()


print("================================================")
print("wokring...")

for i in range(vote_count_needed):
    print("Programmed to be executed", vote_count_needed, "times")
    print("User email are as follows - ")
    print("================================================================")
    vote()

print("================================================")
print("successfully completed")
