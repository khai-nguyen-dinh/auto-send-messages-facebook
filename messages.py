# -*- coding: utf8 -*-
import sys

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def send_messages(username,password,url,content):
    driver = webdriver.PhantomJS()
    driver.get("http://facebook.com")
    driver.find_element_by_name('email').send_keys(username)
    driver.find_element_by_name('pass').send_keys(password)
    submit = driver.find_element_by_id('u_0_m')
    submit.submit()
    try:
        driver.get(url)
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.NAME, 'body'))
        )
        post = driver.find_element_by_name('body')
        post.click()
        post.send_keys(content)
        time.sleep(3)
        driver.find_element_by_name('send').click()

    finally:
        driver.quit()

def main(argv):

    url = 'https://mobile.facebook.com/messages/read/?tid=mid.1382760659753%3Aacf5ecc7ce9c4c4891'
    if argv ==1:
        content = 'Chúc em buổi sáng tốt lành!'
        send_messages('khainguyen@onfta.com','', url, content)
    if argv ==2:
        content = 'Nhớ ăn cơm và nghỉ ngơi điều độ.'
        send_messages('khainguyen@onfta.com', '', url, content)
    if argv ==3:
        content = 'Tối rồi.'
        send_messages('khainguyen@onfta.com', '', url, content)
    if argv ==4:
        content = 'đi học đi.'
        send_messages('khainguyen@onfta.com', '', url, content)
    if argv ==5:
        content = 'Chúc em ngủ ngon.'
        send_messages('khainguyen@onfta.com', '', url, content)


if __name__ == "__main__":
    main(int(sys.argv[1]))
