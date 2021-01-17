if __name__ == "__main__":
    pass

import variables
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

def rutracker_login():
    driver = webdriver.Firefox()
    driver.get("https://rutracker.org")

    try:
        enter = driver.find_element_by_link_text("Вход1")
        enter.click()
    except NoSuchElementException:
        print("Element not found")

    try:
        enter = driver.find_element_by_link_text("Вход")
        enter.click()
    except NoSuchElementException:
        print("Element not found")

    login = driver.find_element_by_id("top-login-uname")
    login.send_keys(variables.rutracker_log)

    password = driver.find_element_by_id("top-login-pwd")
    password.send_keys(variables.rutracker_pass)

    click = driver.find_element_by_id("top-login-btn")
    click.click()

    search = driver.find_element_by_id("search-text")
    search.send_keys("CCNP SWITCH Portable Command Guide")
    search_click = driver.find_element_by_id("search-submit")
    search_click.click()
    time.sleep(5)
    single_search = driver.find_element_by_partial_link_text('Empson S')
    single_search.click()
    torrent_file = driver.find_element_by_link_text("Скачать .torrent")
    torrent_file.click()

    logout = driver.find_element_by_class_name("log-out-icon")
    logout.click()

    time.sleep(5)

    driver.close()
 

def send_mail():
    driver = webdriver.Firefox()
    driver.get("https://meta.ua")

    try:
        enter = driver.find_element_by_xpath("/html/body/div[2]/section/div[1]/span/a[1]/label")
        enter.click()
    except NoSuchElementException:
        print("Element not found")

    try:
        login = driver.find_element_by_name("login")
        login.send_keys(variables.meta_log)
    except NoSuchElementException:
        print("Element login not found")
    try:
        password = driver.find_element_by_name("password")
        password.send_keys(variables.meta_pass)
    except NoSuchElementException:
        print("Element password not found")
   
    try:
        click = driver.find_element_by_xpath('/html/body/div[3]/article/form/button')
        click.click()
    except NoSuchElementException:
        print("Element Увійти not found")       

    try:
        write_mail = driver.find_element_by_id('id_send_email')
        write_mail.click()
    except NoSuchElementException:
        print("Element Send not found")    

    try:
        send_to = driver.find_element_by_id('send_to')
        send_to.send_keys(variables.mail)
    except NoSuchElementException:
        print("Element Send to not found")    

    try:
        subject = driver.find_element_by_id('subject')
        subject.send_keys("Homework Lekay V.V.")
    except NoSuchElementException:
        print("Element Subject not found")    

    try:
        body = driver.find_element_by_id('body')
        body.send_keys("Test-")
    except NoSuchElementException:
        print("Element Body to not found")   

    try:
        send = driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr[1]/td/table/tbody/tr/td[2]/form/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/input[2]")
        send.click()
    except NoSuchElementException:
        print("Element Send not found")

    time.sleep(5)

    driver.close()


