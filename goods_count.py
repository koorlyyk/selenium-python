from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def check_goods_count() :
    exp = 5
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://testshop.sedtest-school.ru/")
    goods_cards = driver.find_elements(By.CSS_SELECTOR, "div[class='card ml-1 mr-1 mt-2']")
    assert len(goods_cards) == exp, f'Ожидается {exp}, найдено {len(goods_cards)}'
    driver.close()