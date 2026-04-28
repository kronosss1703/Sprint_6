import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderPage(BasePage):
    
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-control")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ')]")
    
    @allure.step("Заполнить первую форму заказа")
    def fill_first_form(self, name, lastname, address, metro, phone):
        self.input_text(self.NAME_FIELD, name)
        self.input_text(self.LASTNAME_FIELD, lastname)
        self.input_text(self.ADDRESS_FIELD, address)
        
        self.click(self.METRO_STATION)
        self.input_text(self.METRO_STATION, metro)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//div[text()='{metro}']"))).click()
        
        self.input_text(self.PHONE_FIELD, phone)
        self.click(self.NEXT_BUTTON)
    
    @allure.step("Заполнить вторую форму заказа")
    def fill_second_form(self, date, rental_period, color, comment):
        self.click(self.DATE_FIELD)
        self.input_text(self.DATE_FIELD, date)
        self.driver.find_element(By.TAG_NAME, "body").click()
        
        self.click(self.RENTAL_PERIOD)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//div[text()='{rental_period}']"))).click()
        
        if color == "black":
            self.click(self.COLOR_BLACK)
        elif color == "grey":
            self.click(self.COLOR_GREY)
        
        self.input_text(self.COMMENT_FIELD, comment)
        self.click_js(self.ORDER_BUTTON)
    
    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_js(self.CONFIRM_BUTTON)
    
    @allure.step("Получить сообщение об успешном заказе")
    def get_success_message(self):
        return self.find_element(self.SUCCESS_MESSAGE).text 