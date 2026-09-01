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
-s:display logs in the console
-v: verbose to get detailed information
-k : to collect the test case with test case name
-m : to collect the test case with test marker name
-n: to run the testcases parallel

pytest.
"""

import random
import string
import json
import pytest
import time




from UIAuto.Pages.signupLoginPage import SignupLogin
from UIAuto.Pages.homePage import HomePage



class TestSignupLogin:

    def handle_dialog(dialog):
        message = dialog.message
        print(f"Message: {message}")
        dialog.accept()


    with open(r"C:\Users\motup\PycharmProjects\PythonProject\Auomation excercise with playwright\UIAuto\Testdata\user_creation_data.json") as file:
        test_data = json.load(file)

    @pytest.mark.uesr_reg
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", test_data)


    def test_do_signup(self,page,data):
        auto = random.choices(string.ascii_lowercase, k=8)
        email = "".join(auto)+"_"+data["email"]
        name = "".join(auto)+" "+data["name"]
        print(f"name:{name} and email:{email}")
        page = page
        signup_login = SignupLogin(page)
        home = HomePage(page)
        #home.navigate("https://www.automationexercise.com/")
        assert home.locator_is_visible(home.home_icon)
        home.click_signup()
        signup_login.do_signup(name,email)
        assert home.page.get_by_text(signup_login.enter_acct_info).is_visible(), "Signup is not loaded"
        #signup_login.fill_signup_account_info_form('Mr', 'msn2121')
        #assert home.page.get_by_text(signup_login.add_info).is_visible(), "Signup is not loaded"#NEW
        #signup_login.fill_signup_address_info('kishore','motupalli','Deloite','hyderabad','banglore','Israel',
                                              #'Andraprdesh','Thirupati','517218','72675436')
        #verify continue button
        #assert signup_login.verify_continue_button(), "Continue button is not loaded"
        #click continue button
        #signup_login.click_continue_button()
        # Verify 'Logged in as username'
        #assert home.verify_logged_in_name(),"'Logged in as username is not visible"
        #click delete account name
        #home.click_delete_account()
        # Verify ACCOUNT DELETED! is visible
        #assert signup_login.verify_account_deleted(),"ACCOUNT DELETED is not visible"
        # Click Continue button
        #signup_login.click_continue()




@pytest.mark.smoke
@pytest.mark.test_alert
#Handling the alerts with dialog single
def test_alert(page):

     try:
        page.locator('[href="#OKTab"]').click()
        page.wait_for_timeout(2000)
        with page.expect_event("dialog") as d:
            page.locator('[onclick="alertbox()"]').click()
        page.wait_for_timeout(2000)
        dialog = d.value
        print(dialog.message)
        print(dialog.type)
        dialog.accept()
     except Exception as e:
        print(f"Got the execution: {e}")
     try:
         page.locator('[href="#CancelTab"]').click()
         page.wait_for_timeout(2000)
         with page.expect_event("dialog") as d:
             page.locator('[onclick="confirmbox()"]').click()

         page.wait_for_timeout(2000)
         dialog = d.value
         print(dialog.type)
         print(dialog.message)
         dialog.accept()
     except Exception as e:
         print(f"exception: {e}")
     page.locator('[href="#Textbox"]').click()
     page.wait_for_timeout(2000)
     with page.expect_event('dialog') as d:
         page.locator('[onclick="promptbox()"]').click()
     page.wait_for_timeout(2000)
     dialog = d.value
     dialog.accept("hello")
     
     page.locator('[href="#CancelTab"]').click()
     page.wait_for_timeout(2000)
     page.on("dialog", handle_dialog)
     # once, on
     page.wait_for_selector('//div[@id="CancelTab"]/button').click()
     page.wait_for_timeout(2000)


@pytest.mark.test_alerts_default
def test_alerts_default(page):
    page.locator('[href="#CancelTab"]').click()
    page.wait_for_timeout(2000)
    page.locator('[onclick="confirmbox()"]').click()
    page.wait_for_timeout(2000)
    time.sleep(10)

class TestSignupLogin:
    def handle_filedownload(self,download):
        file_path = './test.zip'
        download.save_as(file_path)
    with open(r"C:\Users\motup\PycharmProjects\PythonProject\Auomation excercise with playwright\UIAuto\Testdata\user_creation_data.json") as file:
        test_data = json.load(file)

    @pytest.mark.fileupload
    def test_file_upload(self, page):
        page.goto('https://demo.automationtesting.in/FileUpload.html')

        # single file upload
        page.query_selector('[id="input-4"]').set_input_files(
            r"C:\Users\motup\OneDrive\Desktop\ABC id.jpg")
        # upload multiple files
        page.query_selector('[id="input-4"]').set_input_file(
            [r"C:\Users\motup\OneDrive\Desktop\ABC id.jpg",
             r"C:\Users\madhusudhana_naidu\Desktop\Profile.png"])
        page.wait_for_timeout(2000)

    @pytest.mark.filedownload
    def test_file_download(self, page):
        page.goto('https://demo.automationtesting.in/FileDownload.html')
        page.wait_for_selector('[id="textbox"]').fill('hello this is file download example')
        page.wait_for_selector('[id="createTxt"]').click()
        page.on('download', self.handle_filedownload)
        page.wait_for_selector('[id="link-to-download"]').click()
        with page.expect_download() as d:
            page.wait_for_selector('[id="link-to-download"]').click()
        download_info = d.value
        download_info.save_as("test_one.zip")
        page.query_selector('[id="input-4"]').set_input_files(r"C:\Users\motup\OneDrive\Desktop\ABC id.jpg")
        page.wait_for_timeout(2000)










