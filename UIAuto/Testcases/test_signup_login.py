"""
as per the pytest conventions test filename,test class name,
test definition must be starts with test

fixtures:
we can write setup and teardown in fixtures
we can write the fixtures in the conftest.py file
we can call fixture as an argument
ex:opening browser is set up and closing the browser at the end is teardown
fixtures scope: function , class, module , session , package

assert : we can use for verification
actual testing done by using assertion


pytest testpath -s -v
-s:display logs in the consloe
-v: verbose to get detailed information
-k : to collect the test case with test case name
-m : to collect the test case with test marker name
-n: to run the testcases parallel

pytest.



"""
from UIAuto.Pages.signupLoginPage import SignupLogin
from UIAuto.Pages.homePage import HomePage



class TestSignupLogin:

    def test_do_signup(self,page):
        page = page
        signup_login = SignupLogin(page)
        home = HomePage(page)
        home.navigate("https://www.automationexercise.com/")
        assert home.locator_is_visible(home.home_icon)
        home.click_signup()
        signup_login.do_signup("ram","ram@gmail.com")
        assert home.page.get_by_text(signup_login.enter_acct_info).is_visible(), "Signup is not loaded"
        signup_login.fill_signup_account_info_form('Mr', 'msn2121')
        assert home.page.get_by_text(signup_login.add_info).is_visible(), "Signup is not loaded"#NEW
        signup_login.fill_signup_address_info('kishore','motupalli','Deloite','hyderabad','banglore','Israel',
                                              'Andraprdesh','Thirupati','517218','72675436')
        #verify continue button
        assert signup_login.verify_continue_button(), "Continue button is not loaded"
        #click continue button
        signup_login.click_continue_button()
        # Verify 'Logged in as username'
        assert home.verify_logged_in_name(),"'Logged in as username is not visible"
        #click delete account name
        home.click_delete_account()
        # Verify ACCOUNT DELETED! is visible
        assert signup_login.verify_account_deleted(),"ACCOUNT DELETED is not visible"
        # Click Continue button
        #signup_login.click_continue()










