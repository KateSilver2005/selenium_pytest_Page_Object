# selenium_pytest_Page_Object
>Page Object Model или кратко Page Object — это паттерн программирования, который очень популярен в автоматизации тестирования и является одним из стандартов при автоматизации тестирования веб-продуктов. 
<br/>Основная идея состоит в том, что каждую страницу веб-приложения можно описать в виде объекта класса. Способы взаимодействия пользователя со страницей можно описать с помощью методов класса. 
<br/>В идеале тест, который будет использовать Page Object, должен описывать бизнес-логику тестового сценария и скрывать Selenium-методы взаимодействия с браузером и страницей. 
<br/>При изменениях в верстке страницы не придется исправлять тесты, связанные с этой страницей. Вместо этого нужно будет поправить только класс, описывающий страницу.  
<br/>Тесты должны быть просто и понятно написаны, а повторяющиеся куски кода выделены в отдельные функции. 
> В Page Object мы отделяем логику действий, например, авторизовать пользователя, от конкретной реализации (найти поле почты, ввести туда данные, найти поле пароля, ввести туда данные, найти кнопку и т.д.). 
</br>Было бы удобно выделить все методы, которые логически относятся к одной веб-странице в нашем продукте, в отдельный класс в нашем коде. 
<br/>Отсюда и название Page Object — это абстрактный объект, который содержит в себе методы для работы с конкретной веб-страницей. 

>*Важно!* Обычно методы у Page Object бывают двух типов: сделать что-то и проверить что-то.
> Рассмотрим страницу товара в [интернет магазине](http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/)
> Какие могут быть методы у Page Object, ассоциированного с такой страницей? Запишем основные сценарии:
> - добавить в корзину;
> - проверить, что есть сообщение об успешном добавлении в корзину;
> - перейти к написанию отзыва;
> - проверить, что есть название, цена, описание товара;
> - вернуться на главную.
><br/>Обратите внимание, что все проверки у нас тоже становятся отдельными методами. 
<br/>В самом тест-кейсе не остается никаких вспомогательных слов типа assert, только описание шагов. 
<br/>Прямо как в нашей тестовой документации.  
> Тесты будут выглядеть примерно так:
```
def test_add_to_cart(browser):
    page = ProductPage(url="", browser)   # инициализируем объект Page Object
    page.open()                           # открываем страницу в браузере
    page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину
    page.add_product_to_cart()            # жмем кнопку добавить в корзину 
    page.should_be_success_message()      # проверяем что есть сообщение с нужным текстом
```
## Подготовка окружения
1. Создайте отдельный публичный репозиторий с осмысленным названием на GitHub.
2. Склонируйте его к себе на локальную машину. 
3. Добавьте туда файл conftest.py из предыдущего модуля. Убедитесь дополнительно, что там есть параметр для задания языка интерфейса, по умолчанию равный "en". 
4. Убедитесь что ни во вложенных папках, ни во внешних папках нет других файлов conftest.py, почему это важно смотри здесь: Conftest.py — конфигурация тестов. 
5. Добавьте в репозиторий файл requirements.txt из предыдущего модуля. 
6. Создайте пустой файл __init__.py, чтобы работали относительные импорты. 
7. Создайте файл test_main_page.py и добавьте в него тест из предыдущего модуля: 
    ```
    def test_guest_can_go_to_login_page(browser):
        link = "http://selenium1py.pythonanywhere.com/"
        browser.get(link)
        login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click() 
    ```
8. Не забудьте активировать окружение, которое мы создали ранее. Опционально, можно создать для этого проекта новое виртуальное окружение для удобства. В таком случае убедитесь что вы установили туда все необходимые пакеты из requirements.txt. А еще не стоит добавлять файлы окружения в репозиторий и вообще в отслеживаемые — лишние файлы на GitHub это моветон. 
9. Убедитесь, что тест работает, с помощью следующей команды: ``pytest -v --tb=line --language=en test_main_page.py``. Здесь и далее мы будем использовать эту команду для запуска. В этой команде мы использовали опцию PyTest --tb=line, которая указывает, что нужно выводить только одну строку из лога каждого упавшего теста. Так вам будет проще разобраться в том, как выглядят сообщения об ошибках. 
10. Добавьте все новые файлы в Git командой ``git add *``
11. Проверьте, что нужные файлы попали в планируемый коммит: ``git status ``
12. Зафиксируйте изменения коммитом с осмысленным сообщением: ``git commit -m "write your message"``. 
13. По желанию добавьте описание репозитория с описанием вашего тестового проекта.

## Базовая страница для проекта: BasePage
Давайте перепишем тест из файла test_main_page.py с помощью паттерна Page Object, который мы добавили на этапе подготовки окружения. <br/>
Мы будем работать с главной страницей нашего приложения, поэтому дадим классу говорящее название MainPage. 

>*Важно!* В этом уроке мы напишем самостоятельно простую реализацию паттерна Page Object. 
<br/>А в следующих уроках уже рассмотрим существующие фреймворки и то, как они могут облегчить нам жизнь. 
<br/>Сейчас самая главная задача — осознать принципы работы. 


1. Создайте в своем проекте папку pages, там мы будем хранить все наши Page Object
2. В папке создайте два файла: ``base_page.py`` и ``main_page.py``
Для начала сделаем базовую страницу, от которой будут унаследованы все остальные классы. В ней мы опишем вспомогательные методы для работы с драйвером.
3. В файле ``base_page.py`` создайте класс с названием BasePage.
В Python такие вещи делаются с помощью следующей конструкции:
``class BasePage():``
4. Теперь в наш класс нужно добавить методы. Первым делом добавим конструктор — метод, который вызывается, когда мы создаем объект. 
<br/>Конструктор объявляется ключевым словом ``__init__``. В него в качестве параметров мы передаем экземпляр драйвера и url адрес. 
<br/>Внутри конструктора сохраняем эти данные как аттрибуты нашего класса. Получается примерно так: 
    ```
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    ```
5. Теперь добавим еще один метод open. Он должен открывать нужную страницу в браузере, используя метод get().

Объявите ниже в том же классе:
    ```
    def open(self):
        self.browser.get(self.url)
    ```
6. Добавьте новые файлы в Git и зафиксируйте изменения коммитом (не забудьте осмысленное сообщение).

В итоге у вас должен следующий код в файле base_page.py: 
```
class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self): 
        self.browser.get(self.url)
```

## Page Object для главной страницы сайта
Теперь реализуем Page Object, который будет связан с главной страницей интернет-магазина. 

1. Откройте файл main_page.py
2. В нем нужно сделать импорт базового класса BasePage: ``from .base_page import BasePage``
3. В нем создайте класс ``MainPage``. Его нужно сделать наследником класса ``BasePage``. Класс-предок в Python указывается в скобках:
    ``class MainPage(BasePage): ``
таким образом, класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка.
4. Перенесите метод из предыдущего урока в класс MainPage:
    ```
    def go_to_login_page(browser):
       login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
       login_link.click() 
    ```
Чтобы все работало, надо слегка видоизменить его. В аргументы больше не надо передавать экземпляр браузера, мы его передаем и сохраняем на этапе создания Page Object. 
<br/>Вместо него нужно указать аргумент self , чтобы иметь доступ к атрибутам и методам класса: ``def go_to_login_page(self):``
Так как браузер у нас хранится как аргумент класса BasePage, обращаться к нему нужно соответствующим образом с помощью self: 
``
self.browser.find_element(By.CSS_SELECTOR, "#login_link")
``
Итого, файл main_page.py будет выглядеть так: 
```
from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
```
## Первый тест на основе Page Object
Ура, первый прототип страницы мы уже реализовали! Давайте теперь перепишем тест с помощью Page Object:
1. Откройте файл с вашим тестом ``test_main_page.py``

2. В самом верху файла нужно импортировать класс, описывающий главную страницу: ``from .pages.main_page import MainPage``
3. Теперь преобразуем сам тест в ``test_main_page.py``: 
    ```
        from .pages.main_page import MainPage
    
    
        def test_guest_can_go_to_login_page(browser):
            link = "http://selenium1py.pythonanywhere.com/"
            page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
            page.open()                      # открываем страницу
            page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
   ```
4. Убедитесь, что тест проходит, запустив его все той же командой:
``pytest -v --tb=line --language=en test_main_page.py``
5. Добавьте изменения и сделайте коммит (с осмысленным сообщением!)

![Структура](https://github.com/KateSilver2005/selenium_pytest_Page_Object/blob/main/images_for_Read_me/1.jpg "Структура")

## Методы-проверки в Page Object
Давайте теперь автоматизируем другой тест-кейс и посмотрим на его примере, как делать методы-проверки. 

Допустим, нам нужно проверять такой сценарий:
1. Открыть главную страницу 
2. Проверить, что есть ссылка, которая ведет на логин 
<br/>Для этого в классе MainPage нужно реализовать метод, который будет проверять наличие ссылки. 
<br/>Обычно все такие методы-проверки называются похожим образом, мы будем называть их should_be_(название элемента). 

Итак, в классе ``MainPage`` создайте метод ``should_be_login_link``. 

Для первой пробы можно реализовать его самым примитивным образом: 
```
def should_be_login_link(self):
    self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
```
Сейчас мы намеренно сделали селектор неправильным, чтобы посмотреть, что именно выдаст тест, если поймает баг. 
<br/>Это хорошая практика: писать сначала красные тесты и только потом делать их зелеными.  

Добавляем в файл с тест-кейсами новый тест: 
```
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
```
Запустите получившийся тест: ``pytest -v --tb=line --language=en test_main_page.py``
<br/>Вывод об ошибке не очень понятный, правда? Разобраться, что именно пошло не так, довольно тяжело. 
<br/>Поэтому в следующем шаге нам нужно будет обработать исключение, которое выбрасывает WebDriver. 

## Проверка элемента на странице
Чтобы выводить адекватное сообщение об ошибке, мы будем все проверки осуществлять с помощью assert и перехватывать исключения.
Для этого напишем вспомогательный метод поиска элемента в нашей базовой странице BasePage, который будет возвращать нам True или False. 
<br/>Можно сделать это по-разному (с настройкой явных или неявных ожиданий). Сейчас воспользуемся неявным ожиданием.

1. В конструктор BasePage добавим команду для неявного ожидания со значением по умолчанию в 10:
    ```
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    ```
2. Теперь в этом же классе реализуем метод is_element_present, в котором будем перехватывать исключение. 
<br/>В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор). 

Чтобы перехватывать исключение, нужна конструкция try/except: 
```
def is_element_present(self, how, what):
    try:
        self.browser.find_element(how, what)
    except (NoSuchElementException):
        return False
    return True
```
Чтобы импортировать нужное нам исключение, в самом верху файла нужно указать: 
``
from selenium.common.exceptions import NoSuchElementException
``
Отлично! Теперь для всех проверок, что элемент действительно присутствует на странице, мы можем использовать этот метод. 

3. Теперь модифицируем метод проверки ссылки на логин так, чтобы он выдавал адекватное сообщение об ошибке: 
    ```
    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"
   ```
Запустите тесты и посмотрите, что вывод об ошибке стал более понятным: 
<br/>``pytest -v --tb=line --language=en test_main_page.py``
И не забудьте заменить селектор на правильный, чтобы тест снова проходил!
4. Сделайте коммит изменений (с осмысленным сообщением).

## Элементы страниц в паттерне Page Object
Помните, мы говорили о том, что тесты почти соответствуют подходу Page Object?
Сейчас разберемся, почему почти на примере короткой и поучительной истории.
У нас уже есть два тест-кейса, которые так или иначе взаимодействуют со ссылкой на логин. 
<br/>Представим себе ситуацию, что у нас модный быстрый agile: разработчики постоянно вносят изменения в продукт. 
<br/>В какой-то прекрасный момент изменения коснулись и шапки сайта. Вот приходит к вам разработчик с новой ссылкой и говорит протестировать.

Замените линк, на котором запускаются тесты на http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer 

Запустите тесты командой:
<br/>``pytest -v --tb=line --language=en test_main_page.py``
Тесты упали, и теперь нам нужно их поддерживать, то есть чинить. Подберите новый селектор к ссылке на логин.
Нам придется поправить в файле ``main_page.py`` несколько мест, где используется измененный селектор.
Чтобы этого избежать, при проектировании тестов (да и вообще кода) хорошей практикой является выносить селектор во внешнюю переменную.
Давайте этим и займемся:
1. В папке ``pages`` создайте новый файл ``locators.py``
2. Внутри создайте новый класс. Каждый класс будет соответствовать каждому классу ``PageObject``: 
    ```
    from selenium.webdriver.common.by import By


    class MainPageLocators():
        LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ```
теперь каждый селектор — это пара: как искать и что искать. 

3. В файле ``main_page.py`` импортируйте новый класс с локаторами 
    ```
    from .locators import MainPageLocators
    ```
4. Теперь в классе ``MainPage`` замените все строки, где содержится ```"#login_link"``` таким образом:
    ```
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    ```
Обратите внимание здесь на символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать. 

5. Запустите тесты с помощью той же самой команды: 
    <br/> ``pytest -v --tb=line --language=en test_main_page.py``
Они, конечно, снова упадут. Но теперь посчитайте, сколько строк вам нужно будет отредактировать, когда тесты написаны в такой конфигурации? 
<br/>Внесите число во второе поле ответа. 


Итак, *PageObject* — это не только методы, но и элементы.  

Исправлять руками сломанные селекторы во всем проекте — долго и муторно, и есть большой риск забыть и оставить старый селектор. 
<br/>Когда мы выносим селекторы в отдельную сущность, мы уменьшаем время на поддержку тестов и сильно упрощаем себе жизнь в долгосрочной перспективе. 

А ещё спринт спустя промоакция закончилась, и фичу с изменением шапки откатили назад. 
<br/>Теперь ссылка работает так же, как раньше. Удалите ссылку с промоакцией, и верните обычную ссылку для запуска тестов: 
<br/>``link = "http://selenium1py.pythonanywhere.com/"``
Не забудьте вернуть старый селектор #login_link, так чтобы тесты снова проходили. Они нам еще пригодятся! 

## Реализация LoginPage
Если вы хорошо ориентируетесь в тест-дизайне, скорее всего вас немного коробит тест с переходом к логину — там ведь нет никаких проверок. 
<br/>Давайте проверим, что мы действительно перешли на страницу логина. Для этого нам будет нужен новый Page Object. 
<br/>Заодно разберемся, как между ними переключаться в ходе теста. 

Скачайте файл с шаблоном для LoginPage. Добавьте его в папку pages. Внутри есть заглушки для методов проверок: 
```
should_be_login_url
should_be_login_form
should_be_register_form
```
Реализуйте их самостоятельно: 

1. В файле ``locators.py`` создайте класс ``LoginPageLocators ``

2. Подберите селекторы к формам регистрации и логина, добавьте их в класс ``LoginPageLocators``
    ```
       class LoginPageLocators:
          REGISTER_FORM = (By.ID, '#register_form2')
          LOGIN_FORM = (By.ID, '#login_form2')
    ```
3. Напишите проверки, используя эти селекторы. Не забудьте через запятую указать адекватное сообщение об ошибке. 
<br/>Напишите сначала красный тест, чтобы убедиться в понятности вывода. 

4. В методе ``should_be_login_url`` реализуйте проверку, что подстрока "login" есть в текущем url браузера. 
<br/>Для этого используйте соответствующее свойство Webdriver.
    ```
    def should_be_login_url(self):
        assert "login" in self.url.current_url, "this isn’t a login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented" 
   ```
5. Добавьте изменения в коммит с осмысленным сообщением

Теперь посмотрим, как можно осуществлять переход между страницами. 

## Переходы между страницами
Переход можно реализовать двумя разными способами. 

1. *Первый способ*: возвращать нужный Page Object.

Для этого в файле ``main_page.py`` нужно сделать импорт страницы с логином: 
```from .login_page import LoginPage
```
Затем в методе, который осуществляет переход к странице логина, проинициализировать новый объект Page и вернуть его: 
```
def go_to_login_page(self):
    link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    link.click()
    return LoginPage(browser=self.browser, url=self.browser.current_url) 
```
>*Обратите внимание!* При создании объекта мы обязательно передаем ему тот же самый объект драйвера для работы с браузером,
<br/>а в качестве url передаем текущий адрес.

Теперь в тесте нам не нужно думать про инициализацию страницы: она уже создана. 
<br/>Сохранив возвращаемое значение в переменную, мы можем использовать методы новой страницы в тесте:
```
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()
```
*Плюсы* такого подхода: 
- тест выглядит аккуратнее — не нужно инициализировать страницу в теле теста; 
- явно возвращаем страницу — тип страницы ассоциирован с методом; 
- не нужно каждый раз думать в разных тестах про инициализацию страницы — уменьшаем дублирование кода;

*минусы*:
- если у нас копится большое количество страниц и переходов — образуется много перекрестных импортов; 
- большая связность кода — при изменении логики придется менять возвращаемое значение; 
- сложнее понимать код, так как страница инициализируется неявно; 
- образуются циклические зависимости, что часто приводит к ошибкам.

2. *Второй подход*: переход происходит неявно, страницу инициализируем в теле теста: 

1. Закомментируйте строку с возвращаемым значением 
```
def go_to_login_page(self):
    link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    link.click()
    # return LoginPage(browser=self.browser, url=self.browser.current_url) 
```

2. Инициализируем LoginPage в теле теста (не забудьте импортировать в файл нужный класс): 

from .pages.login_page import LoginPage
```
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
```
*Плюсы*:
- меньше связность кода; 
- меньше импортов, нет перекрестных импортов; 
- больше гибкость; 
- в тесте понятнее что происходит, т.к. явно инициализируем страницу.

*Минусы*:
- появляется лишний шаг в тест-кейсе; 
- каждый раз при написании теста нужно думать про корректные переходы; 
- дублируется код.

И тот и другой подход можно успешно применять в своих проектах, главное делать это с умом. 
<br/>Сейчас оставьте второй вариант с явной инициализацией страниц в теле теста, чтобы избежать лишних сложностей с циклическими зависимостями. 

Уберите лишний закомментированный код, и зафиксируйте изменения в коммите с осмысленным сообщением.
![Структура](https://github.com/KateSilver2005/selenium_pytest_Page_Object/blob/main/images_for_Read_me/2.jpg "Структура")

## Удобство поддержки тестов — инкапсуляция бизнес-логики в методах
Что делать, если изменилась логика взаимодействия со страницей, которая используется у нас в нескольких тестах? 
<br/>Например, нам нужно проверить возможность перехода на страницу логина по ссылке в навбаре для каждой из страниц сайта. 
<br/>Предположим, что таких страниц 20, и, значит, у нас есть 20 тестов, использующих метод go_to_login_page класса MainPage. 
<br/>Затем разработчики добавили alert, который вызывается при клике на нужную нам ссылку. 
<br/>Мы увидим, что все 20 тестов упали, так как в методе go_to_login_page нет шага с обработкой alert, следовательно, 
<br/>метод should_be_login_page не сработает. Добавив обработку alert в метод go_to_login_page, мы восстановим работоспособность 
<br/>всех тестов, не меняя самих тестов:
```
def go_to_login_page(self):
   link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
   link.click()
   alert = self.browser.switch_to.alert
   alert.accept()
```
Это еще одно преимущество использования паттерна Page Object — мы разделяем сам тест и логику взаимодействия со страницей. 
<br/>Тест становится более читабельным, и его легче поддерживать при изменениях в коде приложения.

## *РЕЗЮМЕ*
- base_page.py - тут мы храним методы которые применяются по всему проекту вообще, всё завернуто в класс, чтобы было удобно импортировать.
- locators.py - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать
- main_page.py - тут мы храним методы по конкретной странице, завернутые в класс этой странице. Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py
- test_main_page.py - тут мы выполняем сами тесты по префиксу "test_"-что это для PyTest. Тут вызванные функции будут запускаться.
    Здесь мы будем создавать функции, которым:
    - выдаём нужный для проверки линк
    - созаём в функции переменную page, которой передаём браузер из base_page.py(класс BasePage) и линк из шага №1
    - следом говорим "page, откройся", но методом из base_page.py(класс BasePage)
    - добавляем проверки, которые создавали методами в main_page.py
# Далее - примочки и лайвхаки в заданиях - [тут](https://stepik.org/lesson/201964/step/1?unit=176022)
![Схема проекта](https://github.com/KateSilver2005/selenium_pytest_Page_Object/blob/main/images_for_Read_me/3.jpg "Схема проекта")

# Генерация тестовых данных в csv-файле - статья с примерами [тут](https://www.ontestautomation.com/writing-tests-for-restful-apis-in-python-using-requests-part-2-data-driven-tests/)
