from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class OrderPage:
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
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def fill_first_form(self, name, lastname, address, metro, phone):
        self.wait.until(EC.element_to_be_clickable(self.NAME_FIELD)).send_keys(name)
        self.driver.find_element(*self.LASTNAME_FIELD).send_keys(lastname)
        self.driver.find_element(*self.ADDRESS_FIELD).send_keys(address)
        
        metro_field = self.driver.find_element(*self.METRO_STATION)
        metro_field.click()
        metro_field.send_keys(metro)
        time.sleep(0.5)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{metro}']"))).click()
        
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone)
        
        next_btn = self.driver.find_element(*self.NEXT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", next_btn)
        time.sleep(0.5)
        next_btn.click()
    
    def fill_second_form(self, date, rental_period, color, comment):
        date_field = self.wait.until(EC.element_to_be_clickable(self.DATE_FIELD))
        date_field.click()
        date_field.clear()
        date_field.send_keys(date)
        self.driver.find_element(By.TAG_NAME, "body").click()
        time.sleep(0.5)
        
        self.wait.until(EC.element_to_be_clickable(self.RENTAL_PERIOD)).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{rental_period}']"))).click()
        
        if color == "black":
            self.driver.find_element(*self.COLOR_BLACK).click()
        elif color == "grey":
            self.driver.find_element(*self.COLOR_GREY).click()
        
        self.driver.find_element(*self.COMMENT_FIELD).send_keys(comment)
        
        time.sleep(1)
        order_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(text(), 'Заказать')]")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", order_btn)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", order_btn)
    
    def confirm_order(self):
        time.sleep(1)
        confirm_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Заказать']")))
        confirm_btn.click()
        
    def get_success_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).text