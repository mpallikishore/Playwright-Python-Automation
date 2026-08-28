#from basePage import BasePage
from UIAuto.Pages.basePage import BasePage


class HomePage(BasePage):
    home_icon = '[class="fa fa-home"]'
    product_link = '[href="/products"]'
    carts_link = '[href="/view_cart"]'
    signup_login_link = '[href="/login"]'
    login_username  = ' Logged in as '
    delete_account_btn = '[href="/delete_account"]'


    def launch_url(self,url):
        self.navigate(url)


    def locator_is_visible(self,locator):
        return self.is_visible(locator)

    def click_signup(self):
        self.click(self.signup_login_link)

    def verify_logged_in_name(self):
        return self.page.get_by_text(self.login_username).is_visible()

    def click_delete_account(self):
        self.page.locator(self.delete_account_btn).click()




