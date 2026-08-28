from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=60000)
    #browser1 = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.automationexercise.com/")
    #page.get_by_role("link",name=" Products").click()
    #page.get_by_placeholder(text='Search Product').fill('shirt')
    #page.get_by_text(text=' Cart').first.click()
    expect(page.locator('[class="fa fa-home]"')).to.be.visible(timeout=10)



