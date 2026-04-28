import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_TOP_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_UltraBig__UU3bP')]")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    
    MAIN_PAGE_URL = "https://qa-scooter.praktikum-services.ru/"
    
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
    
    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open(self.MAIN_PAGE_URL)
    
    @allure.step("Принять куки")
    def accept_cookies(self):
        try:
            self.click(self.COOKIE_BUTTON)
        except:
            pass
    
    @allure.step("Нажать кнопку Заказать (верхняя)")
    def click_order_top(self):
        self.click(self.ORDER_TOP_BUTTON)
    
    @allure.step("Нажать кнопку Заказать (нижняя)")
    def click_order_bottom(self):
        self.scroll_to_element(self.ORDER_BOTTOM_BUTTON)
        self.click_js(self.ORDER_BOTTOM_BUTTON)
    
    @allure.step("Кликнуть на вопрос {question_num}")
    def click_question(self, question_num):
        question_locator = getattr(self, f"QUESTION_{question_num}")
        self.click(question_locator)
    
    @allure.step("Получить текст ответа {answer_num}")
    def get_answer_text(self, answer_num):
        answer_locator = getattr(self, f"ANSWER_{answer_num}")
        return self.find_element(answer_locator).text
    
    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)
    
    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)
    
    @allure.step("Получить URL главной страницы")
    def get_main_page_url(self):
        return self.MAIN_PAGE_URL