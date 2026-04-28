from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)
    
    @allure.step("Найти элемент {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step("Кликнуть на элемент {locator}")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    @allure.step("Заполнить поле {locator} значением {text}")
    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Переключиться на окно с индексом {index}")
    def switch_to_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])
    
    @allure.step("Скролл к элементу {locator}")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    @allure.step("Кликнуть через JS на {locator}")
    def click_js(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)