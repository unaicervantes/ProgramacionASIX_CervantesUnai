#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def main():
    url = 'https://es.wikipedia.org/wiki/Wikipedia:Portada'
    wikipedia_request = requests.get(url)
    if not wikipedia_request.ok:
        print("Error: " + str(wikipedia_request.status_code))
        quit()
    sopa_wikipedia = BeautifulSoup(wikipedia_request.text, 'html.parser')
    articulo_destacado = sopa_wikipedia.find(id='Artículo_destacado').parent.find(class_='main-header main-box-header').text
    articulo_bueno = sopa_wikipedia.find(id='Artículo_bueno').parent.find(class_='main-header main-box-header').text
    print('Artículo destacado: ' + articulo_destacado)
    print('Artículo bueno: ' + articulo_bueno)


    driver = webdriver.Firefox()
    driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")
    elem = driver.find_element(By.ID, 'Artículo_destacado') \
                .find_element(By.XPATH, './..') \
                .find_element(By.CSS_SELECTOR, 'a')
    elem.click()
    input("Continua")
    driver.close()

    driver = webdriver.Firefox()
    driver.get("https://github.com/")
    
    elem = driver.find_element(By.LINK_TEXT, "Sign in").click()
    elem = driver.find_element(By.ID, 'login_field').send_keys("f.javier.quesada@iesjoandaustria.org")
    elem = driver.find_element(By.ID, 'password').send_keys(os.environ['PASSWORD_GITHUB'])
    elem = driver.find_element(By.CLASS_NAME, 'js-sign-in-button').click()
    time.sleep(3)
    elem = driver.find_element(By.CLASS_NAME, "news")
    activitats = elem.find_elements(By.XPATH, "//div[@class='d-flex flex-column width-full']")
    for activitat in activitats:
        print('--- --- --- --- --- --- ---')
        print('*** *** *** *** *** *** ***')
        print(activitat.text) 
        print('*** *** *** *** *** *** ***')
        print('--- --- --- --- --- --- ---')

    # driver = webdriver.Firefox()
    # driver.get("https://www.netflix.com/es/")
    # try:
    #     elem = driver.find_element(By.CLASS_NAME, 'close-button')
    #     elem.click()
    # except:
    #     pass
    # elem = driver.find_element(By.LINK_TEXT, "Iniciar sesión").click()
    # elem = driver.find_element(By.ID, 'id_userLoginId').send_keys("?@gmail.com")
    # elem = driver.find_element(By.ID, 'id_password').send_keys(os.environ['PASSWORD_NFX'])
    # elem = driver.find_element(By.CLASS_NAME, 'login-button').click()
    
    input("Continua")

    
if __name__ == "__main__":
    main()
    