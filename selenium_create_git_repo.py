# Selenium script to create new github repo
from selenium import webdriver

browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')


def git_hub_login():
    username = ''
    password = ''
    browser.get('https://github.com/login')

    email_button = browser.find_element_by_id('login_field')
    email_button.send_keys(username)
    password_button = browser.find_element_by_id('password')
    password_button.send_keys(password)

    login_button = browser.find_element_by_name('commit')
    login_button.click()


def create_repo(name):
    browser.get('https://github.com/new')

    # name_button = browser.find_elements_by_xpath("//input[@name='repository[name]']")[0]
    name_button = browser.find_element_by_id('repository_name')
    name_button.send_keys(name)
    python_button = browser.find_element_by_css_selector('button.first-in-line')
    python_button.submit()


git_hub_login()
create_repo('test0')
browser.quit()
