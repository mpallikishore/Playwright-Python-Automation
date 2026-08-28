
"""
this is the way we are writing the page object design pattern model we're writing the code
by this we can make the changes easily at any point of time we can easily understand then we want to change
for example:
 we want made changes in the signup page we can change
"""




#from basePage import BasePage
from UIAuto.Pages.basePage import BasePage

#we will write all the locators and methods for signup and login features
class SignupLogin(BasePage):
    signup_login_link = '[href="/login"]'
    new_user_signup = '"new user signup!"'
    name = '[data-qa="signup-name"]'
    email = '[data-qa="signup-email"]'
    submit_btn = '[data-qa="signup-button"]'


    #Enter Account Information
    enter_acct_info = 'Enter Account Information'
    mr_btn = '[id="id_gender1"]'
    mrs_btn = '[id="id_gender2"]'
    password_field = '[name="password"]'
    days_dp = '[id="days"]'
    months_dp = '[id="months"]'
    years_dp = '[id="years"]'
    news_letter_check = '[id="newsletter"]'
    receive_options_check = '[id="optin"]'


    #Address Information
    add_info = 'Address Information'
    first_name = '[name="first_name"]'
    last_name = '[name="last_name"]'
    company_name = '[name="company"]'
    add_info1 = '[name="address1"]'
    add_info2 = '[name="address2"]'
    country_dp = '[id="country"]'
    state_name = '[name="state"]'
    city_name = '[name="city"]'
    zip_code = '[name="zipcode"]'
    mobile_number = '[name="mobile_number"]'
    create_btn = '[data-qa="create-account"]'
    continue_btn = '[data-qa="continue-button"]'

    def enter_username(self,username):
        self.fill(self.name,username)

    def enter_email(self,email):
        self.fill(self.email,email)

    def click_login(self):
        self.click(self.submit_btn)

    def click_create_account(self):#NEW
        self.click(self.create_btn)


    def do_signup(self,username,email):
        print("***** do login started *******")
        self.enter_username(username)
        self.enter_email(email)
        self.click_login()
        print("***** do login ended *******")

    def fill_signup_account_info_form(self,title,password):#Fill details: Title, Password, Date of Birth
        print("***** fill signup form started *******")
        if title == 'Mr':
            self.click(self.mr_btn)
        else:
            self.click(self.mrs_btn)
        self.fill(self.password_field, password)
        self.select_dropdown_option(self.days_dp, '10', 'value')
        self.select_dropdown_option(self.months_dp, 'August', 'label')
        self.select_dropdown_option(self.years_dp, dropdown_value='1996', dropdown_value_type='value')
        self.check_checkbox(self.news_letter_check)
        self.check_checkbox(self.receive_options_check)
        print("******** fill signup form is ended *******")

    def fill_signup_address_info(self, firstname, lastname, company, address1, address2, country,
                                 state,city, zipcode, mobile):
        print("***** fill address info started *******")
        self.fill(self.first_name,firstname)
        self.fill(self.last_name,lastname)
        self.fill(self.company_name,company)
        self.fill(self.add_info1,address1)
        self.fill(self.add_info2,address2)
        self.select_dropdown_option(self.country_dp,country,'label')
        self.fill(self.state_name,state)
        self.fill(self.city_name,city)
        self.fill(self.zip_code,zipcode)
        self.fill(self.mobile_number,mobile)
        self.click(self.create_btn)#NEW
        print("******* account created successfully *******")

    def verify_continue_button(self):
        return self.is_visible(self.continue_btn)

    def click_continue_button(self):
        self.page.locator(self.continue_btn).click()

    def verify_account_deleted(self):
        return self.page.get_by_text("ACCOUNT DELETED!").is_visible()

    #def click_continue(self):
        #self.page.locator(self.continue_btn).click()



















