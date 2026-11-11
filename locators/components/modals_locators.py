from selenium.webdriver.common.by import By


class LocatorsForModals:
    """ Локаторы для глобавльных модалок (Заказать звонок, Быстрый просмотр, Задать вопрос) """

    #    Локаторы для перехода на модалки:
    BTN_CALL_ME = (By.CSS_SELECTOR, 'div[class="animate-load btn btn-default btn-wide btn-sm has-ripple"]')  # Кнопка "Заказать звонок" в хедере
    # IMG_CARD = (By.CSS_SELECTOR, 'div.sticker--upper')  # Фото карточки товара на странице (чтобы попасть на кнопку - надо навести курсор на фото)
    # BTN_FAST_WATCH = (By.CSS_SELECTOR, 'div.btn-default[data-name="fast_view"]')  # Кнопка "Быстрый просмотр"
    #    (там много совпадений, т.к. кнопка переиспользуется: возможно понадобится либо методом в первую проваливаться,
    #        либо ХПАСОМ индекс первой же кнопки забирать)

    #     --- IFrame и элементы капчи ---
    CAPTCHA_IFRAME = (By.CSS_SELECTOR, 'iframe[data-testid="checkbox-iframe"]')  # Капча "Я не робот" (её контейнер)
    CAPTCHA_CHECKBOX = (By.CSS_SELECTOR, 'div.CheckboxCaptcha-Checkbox')  # Галочка внутри капчи "Я не робот"
    CHECKBOX_COFIDENTIONAL = (By.XPATH, '(//div[@class="CheckboxCaptcha-Checkbox"])[1]')  # Чекбокс согласия с политикой сайта


    # --- Модалка "Заказать звонок" ---
    MODAL_CALLBACK = (By.CSS_SELECTOR, 'div.callback_frame')  # Контейнер модалки (сама модалка_div)
    INPUT_CALLBACK_NAME = (By.CSS_SELECTOR, 'input[id="POPUP_NAME"]')  # Поле "Ваше имя"
    INPUT_CALLBACK_PHONE = (By.CSS_SELECTOR, 'input[id="POPUP_PHONE"]')  # Поле "Телефон"
    BTN_CALLBACK_SUBMIT = (By.CSS_SELECTOR, 'input.btn-default[name="web_form_submit"]')  # Кнопка "Отправить"
    ERROR_MSG_NAME = (By.CSS_SELECTOR, 'label[id="POPUP_NAME-error"]')  # Сообщение под пустым полем "Ваше имя": Заполните это поле!
    ERROR_MSG_PHONE = (By.CSS_SELECTOR, 'label[id="POPUP_PHONE-error"]')  # Сообщение под пустым полем "Телефон": Заполните это поле!
    ERROR_MSG_CAPCHA = (By.CSS_SELECTOR, 'label[id="-error"]')  # Сообщение под пустым полем "Капча": Пройдите проверку
    ERROR_MSG_COFIDENTIONAL = (By.CSS_SELECTOR, 'label[id="licenses_popup-error"]')  # Сообщение под пустым полем "Политика сайта": Согласитесь с условиями

    # --- Модалка "Быстрый просмотр" --- (добавить также локаторых других элементов модалки, чтоб +- всё проверить можно было)
    BTN_DETAILED_QUICK_VIEW = (By.CSS_SELECTOR, 'div.scrollbar a[title="Подробнее о товаре"]')  # Кнопка "Подробнее о товаре"
    MODAL_QUICK_VIEW = (By.CSS_SELECTOR, 'div[class="fast_view_frame jqmWindow popup jqm-init show"]')  # Контейнер модалки (сама модалка_div)
    TITLE_QUICK_VIEW = (By.CSS_SELECTOR, 'a.catalog-detail__title')  # Заголовок_название товара
    BTN_QUICK_VIEW_IN_FAVORITE = (By.CSS_SELECTOR, '.line-block__item .item-action--favorite')  # Кнопка "В избранное"
    BTN_QUICK_VIEW_IN_COMPARE = (By.CSS_SELECTOR, '.line-block__item .item-action--compare')  # Кнопка "В сравнение"
    BTN_QUICK_VIEW_IN_BASKET = (By.CSS_SELECTOR, 'div.scrollbar span[data-action="basket"]')  # Кнопка "В корзину"
    BTN_QUICK_VIEW_BYE_IN_ONE_CLICK = (By.CSS_SELECTOR, 'div.scrollbar span[data-event="jqm"]')  # Кнопка "Купить в 1 клик"
    BTN_QUICK_VIEW_CLOSE = (By.CSS_SELECTOR, 'span.jqmClose i.svg.inline')  # Кнопка закрытия модалки
    BTN_PREV_CARD = (By.CSS_SELECTOR, 'div.fast-view-nav[data-fast-nav="prev"]')  # Кнопка "Предыдущий товар"
    BTN_NEXT_CARD = (By.CSS_SELECTOR, 'div.fast-view-nav[data-fast-nav="next"]')  # Кнопка "Слудующий товар"
    MODAL_BYE_IN_ONE_CLICK = (By.CSS_SELECTOR, '.scrollbar#one_click_buy')  # Контейнер модалки "Купить в 1 клик" (сама модалка_div)
    TITLE_MODAL_BYE_IN_ONE_CLICK = (By.XPATH, '(//div[text()="Купить в 1 клик"])')
    #    этот локатор будет падать 100%, т.к. если я обращусь к нему где-нибудь в другом месте по индексу, где другое количество этих кнопок - он упадёт
    #         нужно будет его уникальным сделать