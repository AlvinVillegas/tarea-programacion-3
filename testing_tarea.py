from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pytest import mark
import time
from datetime import datetime
from selenium import webdriver

def login():
    driver = webdriver.Chrome()
    driver.get("https://um.froid.works/admin/index.php")
    usuario = driver.find_element(By.ID, 'username')
    contraseña = driver.find_element(By.ID, 'password')
    boton = driver.find_element(By.XPATH, '//button[@type="submit"]')
    driver.maximize_window()
    usuario.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    usuario.send_keys('admin')
    contraseña.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    contraseña.send_keys('admin')
    boton.click()
    return driver

@mark.parametrize("usu,contra", [("admin", "admin"), ("fail", "fail"), ("admin", "12345"), ("a", "data")])
def testing_login(usu,contra):
    driver = webdriver.Chrome()
    driver.get("https://um.froid.works/admin/index.php")
    usuario = driver.find_element(By.ID, 'username')
    contraseña = driver.find_element(By.ID, 'password')
    boton = driver.find_element(By.XPATH, '//button[@type="submit"]')
    driver.maximize_window()
    usuario.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    usuario.send_keys(usu)
    contraseña.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    contraseña.send_keys(contra)
    boton.click()
    hora = datetime.now().strftime("%H-%M-%S")
    driver.save_screenshot('./img/login/foto'+hora+'.png')
    time.sleep(3)
    assert driver.current_url != "https://um.froid.works/admin/index.php"

def testing_adminconfig():
    driver = login()
    time.sleep(5)
    driver.find_element(By.XPATH, '//div[@class="top-menu"]/ul').click()
    driver.find_element(By.XPATH, '//div[@class="top-menu"]//ul//li/ul/li[1]/a').click()
    name = driver.find_element(By.XPATH, '//form//input[@id="name"]').get_attribute('value')
    hora = datetime.now().strftime("%H-%M-%S")
    driver.save_screenshot('./img/adminconfig/foto'+hora+'.png')
    assert name == 'Admin'

def testing_logout():
    driver = login()
    time.sleep(5)
    driver.find_element(By.XPATH, '//div[@class="top-menu"]/ul').click()
    driver.find_element(By.XPATH, '//div[@class="top-menu"]//ul//li/ul/li[3]/a').click()
    hora = datetime.now().strftime("%H-%M-%S")
    driver.save_screenshot('./img/adminconfig/foto'+hora+'.png')
    assert driver.current_url == "https://um.froid.works/admin/index.php"

def testing_userbtn():
    driver = login()
    time.sleep(5)
    driver.find_element(By.XPATH, '//ul[@class="page-sidebar-menu   "]/li[2]/a').click()
    hora = datetime.now().strftime("%H-%M-%S")
    driver.save_screenshot('./img/logout/foto'+hora+'.png')
    hora = datetime.now().strftime("%H-%M-%S")
    driver.save_screenshot('./img/logout/foto'+hora+'.png')
    assert driver.current_url == 'https://um.froid.works/admin/users.php'

def testing_configbtn():
    driver = login()
    time.sleep(5)
    driver.find_element(By.XPATH, '//ul[@class="page-sidebar-menu   "]/li[3]/a').click()
    hora = datetime.now().strftime("%H-%M-%S")
    driver.save_screenshot('./img/logout/foto'+hora+'.png')
    hora = datetime.now().strftime("%H-%M-%S")
    driver.save_screenshot('./img/configbtn/foto'+hora+'.png')
    assert driver.current_url == 'https://um.froid.works/admin/page_settings.php'
