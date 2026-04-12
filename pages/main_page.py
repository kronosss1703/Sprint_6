from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    # Локаторы
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")  # Кнопка "да все привыкли"
    ORDER_TOP_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")  # Верхняя кнопка Заказать
    ORDER_BOTTOM_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_UltraBig__UU3bP')]")  # Нижняя кнопка
    QUESTION_1 = (By.ID, "accordion__heading-0")
    QUESTION_2 = (By.ID, "accordion__heading-1")
    QUESTION_3 = (By.ID, "accordion__heading-2")
    QUESTION_4 = (By.ID, "accordion__heading-3")
    QUESTION_5 = (By.ID, "accordion__heading-4")
    QUESTION_6 = (By.ID, "accordion__heading-5")
    QUESTION_7 = (By.ID, "accordion__heading-6")
    QUESTION_8 = (By.ID, "accordion__heading-7")
    
    ANSWER_1 = (By.ID, "accordion__panel-0")
    ANSWER_2 = (By.ID, "accordion__panel-1")
    ANSWER_3 = (By.ID, "accordion__panel-2")
    ANSWER_4 = (By.ID, "accordion__panel-3")
    ANSWER_5 = (By.ID, "accordion__panel-4")
    ANSWER_6 = (By.ID, "accordion__panel-5")
    ANSWER_7 = (By.ID, "accordion__panel-6")
    ANSWER_8 = (By.ID, "accordion__panel-7")
    
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
    
    def accept_cookies(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.COOKIE_BUTTON)).click()
        except:
            pass
    
    def click_order_top(self):
        self.wait.until(EC.element_to_be_clickable(self.ORDER_TOP_BUTTON)).click()
    
    def click_order_bottom(self):
        self.driver.find_element(*self.ORDER_BOTTOM_BUTTON).click()
    
    def click_question(self, question_num):
        question_locator = getattr(self, f"QUESTION_{question_num}")
        self.driver.find_element(*question_locator).click()
    
    def get_answer_text(self, answer_num):
        answer_locator = getattr(self, f"ANSWER_{answer_num}")
        self.wait.until(EC.visibility_of_element_located(answer_locator))
        return self.driver.find_element(*answer_locator).text
    
    def click_scooter_logo(self):
        self.driver.find_element(*self.SCOOTER_LOGO).click()
    
    def click_yandex_logo(self):
        self.driver.find_element(*self.YANDEX_LOGO).click()