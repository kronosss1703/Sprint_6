import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Тесты главной страницы")
class TestMainPage:
    
    @allure.story("Вопросы о важном")
    @allure.title("Проверка текста ответов в аккордеоне")
    @pytest.mark.parametrize("question_num, answer_num, expected_text", [
        (1, 1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (2, 2, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (3, 3, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (4, 4, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (5, 5, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (6, 6, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        (7, 7, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (8, 8, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ])
    def test_question_answer(self, driver, question_num, answer_num, expected_text):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        
        main_page.click_question(question_num)
        
        actual_text = main_page.get_answer_text(answer_num)
        assert actual_text == expected_text, f"Текст ответа {question_num} не совпадает"
    
    @allure.story("Логотипы")
    @allure.title("Переход на главную страницу Самоката по клику на логотип")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        
        main_page.click_scooter_logo()
        
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"
    
    @allure.story("Логотипы")
    @allure.title("Переход на Дзен по клику на логотип Яндекса")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        
        main_page.click_yandex_logo()
        
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        
        assert "dzen.ru" in driver.current_url or "yandex" in driver.current_url


@allure.feature("Тесты заказа самоката")
class TestOrderFlow:
    
    @allure.story("Позитивный сценарий заказа")
    @allure.title("Заказ самоката через верхнюю кнопку")
    @pytest.mark.parametrize("name, lastname, address, metro, phone, date, rental_period, color, comment", [
        ("Иван", "Петров", "ул. Ленина 1", "Курская", "89991234567", "25.12.2025", "сутки", "black", "Позвоните за час"),
        ("Анна", "Сидорова", "пр. Мира 10", "Парк культуры", "89997654321", "26.12.2025", "трое суток", "grey", "Домофон 123")
    ])
    def test_order_from_top_button(self, driver, name, lastname, address, metro, phone, date, rental_period, color, comment):
        wait = WebDriverWait(driver, 15)
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        
        main_page.click_order_top()
        
        order_page = OrderPage(driver)
        order_page.fill_first_form(name, lastname, address, metro, phone)
        order_page.fill_second_form(date, rental_period, color, comment)
        order_page.confirm_order()
        
        success_text = order_page.get_success_message()
        assert "Заказ оформлен" in success_text
    
    @allure.story("Позитивный сценарий заказа")
    @allure.title("Заказ самоката через нижнюю кнопку")
    @pytest.mark.parametrize("name, lastname, address, metro, phone, date, rental_period, color, comment", [
        ("Максим", "Иванов", "бульвар Строителей 5", "Новокузнецкая", "89991112233", "27.12.2025", "двое суток", "black", "Не звонить в офис"),
        ("Елена", "Козлова", "пер. Лесной 7", "Воробьёвы горы", "89995556677", "28.12.2025", "четверо суток", "grey", "Код домофона 42")
    ])
    def test_order_from_bottom_button(self, driver, name, lastname, address, metro, phone, date, rental_period, color, comment):
        wait = WebDriverWait(driver, 15)
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        
        bottom_btn = driver.find_element(By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_UltraBig__UU3bP')]")
        driver.execute_script("arguments[0].scrollIntoView(true);", bottom_btn)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", bottom_btn)
        
        order_page = OrderPage(driver)
        order_page.fill_first_form(name, lastname, address, metro, phone)
        order_page.fill_second_form(date, rental_period, color, comment)
        order_page.confirm_order()
        
        success_text = order_page.get_success_message()
        assert "Заказ оформлен" in success_text