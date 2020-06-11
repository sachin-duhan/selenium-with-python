import random
import names
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

POST_URL = "https://app.biorender.com/contest/profile/5dc321790d5929007dfbf7bb-satish-poojary/s-5ed39d568563ce00af3b4cc3-tumor-microenvironment-drives-cancer-progression"
SIGN_UP = "https://app.biorender.com/user/signup"


class User():
    f = names.get_first_name()
    l = names.get_last_name()
    n = random.randint(10, 100)


print("================================")

print("sample test case started")

driver = webdriver.Chrome()
# driver.maximize_window()

driver.get(SIGN_UP)
# time.sleep(3000)
# driver.find_element_by_xpath(
#     "//input[@class='comment-form-unauthenticated__btn-sign-up']").click()


myUser = User()
sign_up_form = {'firstName': myUser.f, 'lastName': myUser.l,
                'email': myUser.f + myUser.l + str(myUser.n) + '@gmail.com',
                'password': 'password'}

driver.implicitly_wait(5)
# sign up form iteration
for key in sign_up_form:
    driver.find_element_by_name(key).send_keys(sign_up_form[key])

driver.find_element_by_class_name(
    "user-form__main-button").send_keys(Keys.ENTER)
driver.close()
print("================================")
print("sample test case successfully completed")
