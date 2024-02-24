import allure
from pages.select_category import category_name
from pages.main_page import main_page


@allure.tag('web')
@allure.label('layer', 'web')
@allure.label('owner', 'e_bashurova')
@allure.story('Выбор товара по категории')
@allure.link('https://www.officemag.ru', name='Test')
@allure.title('Выбор категории "Деловые аксессуары"')
def test_product_category(browser_configs):
    main_page.open_page()
    main_page.product_category('Деловые аксессуары')


@allure.title('Выбор подкатегории "Портфели, сумки, папки из кожи"')
def test_furniture_category(browser_configs):
    main_page.open_page()
    main_page.product_category('Деловые аксессуары')
    category_name.select_subcategory('Портфели, сумки, папки из кожи')


@allure.title('Выбор категории через поиск')
def test_furniture_category(browser_configs):
    main_page.open_page()
    main_page.search_product_by_button("Деловые аксессуары")
