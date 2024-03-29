import allure
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step('Open a browser')
    def open(self):
        self.driver.get(self.url)

    @allure.step('Find a visible element')
    def element_is_visible(self, locator, timeout=5):                      # поиск одного видимого элемента
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Find visible elements')
    def elements_are_visible(self, locator, timeout=5):                     # поиск всех видимых элементов
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Find a present element')
    def element_is_present(self, locator, timeout=6):                       # ждёт появления элемента в DOM дереве
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Find present elements')
    def elements_are_present(self, locator, timeout=6):                     # ждёт появления всех элементов в DOM дереве
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step('Find a not visible element')
    def element_is_not_visible(self, locator, timeout=5):                   # поиск одного невидимого элемента
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Find clickable elements')
    def element_is_clickable(self, locator, timeout=6):                     # для проверок кликабельности элемента
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Go to specified element')
    def go_to_element(self, element):                                       # скролл к выбранному элементу
        self.driver.execute_script("arguments[0].scrollIntoView();", element)  # скрипт джавовый

# DOM - Объектная Модель Документа (Document Object Model) – это программный интерфейс (API) для HTML и XML документов
    @allure.step('Double click')
    def action_double_click(self, element):                                 # двойное нажатие lbm
        action = ActionChains(self.driver)   # библиотека действий с кликами мышки скролом и перетаскивать элементы etc
        action.double_click(element)         # синтаксис, выбор двойного клика левой кнопки мыши
        action.perform()                     # синтаксис, выполнение действия

    @allure.step('Right click')
    def action_right_click(self, element):                                  # клик rbm
        action = ActionChains(self.driver)   # библиотека действий с кликами мышки скролом и перетаскивать элементы etc
        action.context_click(element)        # синтаксис, выбор клика правой кнопкой мыши
        action.perform()                     # синтаксис, выполнение действия

    @allure.step('Drag and drop by offset')
    def action_drag_and_drop_by_offset(self, element, x_coord, y_coord):    # перетягивание элемента (например слайдера, div box) по координатам
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coord, y_coord)
        action.perform()

    @allure.step('Drag and drop to element')
    def action_drag_and_drop_to_element(self, what, where):                 # "what(какой ),where(куда)" меняет местами элементы
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()

    @allure.step('Move cursor to element')
    def action_move_to_element(self, element):                              # перемещение курсора мышки на элемент
        action = ActionChains(self.driver)   # библиотека действий с мышкой (скролл, клик, наведение на элемент etc)
        action.move_to_element(element)      # синтаксис, наведение курсора на элемент
        action.perform()                     # синтаксис, выполнение действия

    @allure.step('Remove footer')
    def remove_footer(self):
        # удаление по тегу - футера страницы (перекрывает кнопку "Submit", по факту это баг)
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        # удаление по id - кнопки в футере страницы
        # self.driver.execute_script("document.getElementsById('close-fixedban').remove();")

