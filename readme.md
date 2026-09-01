""" Create a project folder / repo

Create a virtualenv

windows: create cmd: python -m venv new_venv activation cmd: new_venv/Scripts/activate deactivate: deactivate

To perform the UI Automation we need requirements: Programming language: Python / Java / .net / typescript / javascript etc Web interface / UI automation: Selenium webdriver / Playwright API Testing: Requests / Playwright Design patterns: Page object model( POM ) , Page factory by using pom we can develop a framework which more readable, scalable, reusable componets we can develop Frameworks: Pytest, Robot framework, Behave(Gherkin) etc pytest: filename, class name and test defination name must be starts with test pip install -r requirements.txt

Project: -> UIAuto -> Pages -> basePage.py # comman selenium / playwright methods -> loginPage.py # login page locators, methods -> productPage.py # product locators and methods -> TestCases -> test_login.py -> test_products.py -> Helpers -> Utils -> file_utils.py -> log_parse.py -> string_manipulations.py -> date_manipulations.py -> TestData .json .xlsx .csv .py -> Config config.yaml config.ini config.json
-> APIAuto
-> output
    -> logs
    -> screenshots
    -> reports
-> cicd
    -> jenkins
    -> bamboo
    -> github actions
requirements.txt
    selenium == 3.14
    pytest == 1.54
    playwright
readme.md
    we can have a desc about project and setup project etc
pytest.ini 
    log_level: Info, debug, warning, error
    markers: 
    cmd_options: 
    test_path:
conftest.py
    fixtures: setup and teardown, pre conditions we can use in fixtures
    scopes: function, class, module, session and package
    by default is function scope
    function: it will execute once per the each function / test defination
    class: it will execute only once per the class
    module: it will execute only once per the file / module
    session: it will execute only once per the session
    package: it will execute only once per the package.
    hooks: 
parametrization: it is a pytest feature to run a single testcase with multiple test data
marker: we can use to segregate / group the testcases based on the features


How can handle pop-ups and dialogue boxs,
alerts:
sometimes we can click any button or link i will show any pop message is called alert
1)single button-okay,cancel,accept(by using (Accept method) we can click the okay button )
2)multiple button - yes or no,okay or cacel ,accept or dissmiss
3)sometimes it will take user input to accept or cancel the alert
when we want accept then we will use (accept method)
when we want dismiss then we will use (dismiss method)

In playwright we can handle the popups in two ways



