from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


def test_elems_on_goods_card() :
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://testshop.sedtest-school.ru/product/31/")
    goods_title = driver.find_element(By.CSS_SELECTOR, "h5 > span")
    assert goods_title.text == "Монокуляр Veber 7-21x21W ZOOM"
    goods_image = driver.find_element(By.CSS_SELECTOR, "img[src='/static/products/31.png']")
    assert goods_image.value_of_css_property('width') != 'undefined'
    goods_description = driver.find_element(By.CSS_SELECTOR, 'p[style="color:grey"]')
    adovoe_description = "Монокуляр Veber 7-21x21W ZOOM - компактный оптический прибор для наблюдения за окружающей средой с переменным увеличением 7х-21х. Кто сказал, что в театр ходят только с биноклем? Нарядный, легкий и очень компактный монокуляр Veber 7-21x21 ZOOM в белом корпусе можно взять с собой и на концерт, и на прогулки по городу. Он окажется у Вас под рукой в любой момент, когда захочется лучше рассмотреть какие-либо детали, ведь монокуляр можно держать в кармане куртки, в дамской сумочке или в бардачке машины.Для изготовления призмы оборачивающей системы (Roof) применяется стекло BАK-4 с многослойным просветлением (FMC). Линзы из оптического стекла (также с многослойным просветлением) объектива и окуляра обеспечивают яркое и четкое изображение даже при плохом освещении или в сумерках.Кольцо масштабирования размера изображения (зум) с резиновым колесом прокрутки находится сверху корпуса монокуляра. Параллельно ему находится диоптрийное кольцо с подстройкой под разное зрение."
    assert goods_description.text == adovoe_description
    goods_price = driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > span:nth-child(1)")
    assert goods_price.text == '1999.0 р'
    cart_button = driver.find_element(By.CSS_SELECTOR, '#in_cart_link_31')
    assert cart_button.is_displayed() == True
    favorite_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#in_star_link_31')))
    assert favorite_button.is_displayed() == True
    driver.close()