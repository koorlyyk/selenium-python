from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_auth() :
    exp = 5
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://testshop.sedtest-school.ru/users/auth/")
    login_field = driver.find_element(By.XPATH, '//input[@type="email"]')
    login_field.send_keys('drugoyemeil@gmail.com')
    password_field = driver.find_element(By.XPATH, '//input[@type="password"]')
    password_field.send_keys('qwerty123')
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    logout_button = driver.find_element(By.CSS_SELECTOR, "[href^='/users/logout']")
    assert logout_button.text == "Выйти" #Не нашла надписи Привет, поэтому тут будет проверка на текст в кнопке выхода
    driver.close()