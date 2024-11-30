import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from playwright.sync_api._generated import Page

DRY_RUN = True
HEADLESS = True

load_dotenv()
required_env_vars = [
    "LOGIN",
    "PASSWORD"
]
errs = []
for var in required_env_vars:
    if var not in os.environ:
        err_msg = f"'{var}' environment variable is required"
        errs.append(err_msg)
if len(errs) > 0:
    raise AssertionError(errs)


def login(page: Page):
    login_page_url = "https://ticktick.com/signin"
    print(f"Navigate to the login page: {login_page_url}")
    page.goto(login_page_url)
    print("Fill in username and password")
    page.fill('input[type="text"]', os.environ['LOGIN'])
    page.fill('input[type="password"]', os.environ['PASSWORD'])
    print("Submit the login form")
    page.click('.button__3eXSs')
    page.wait_for_timeout(5000)


def download_with_save(page: Page, css_selector: str):
    if not DRY_RUN:
        with page.expect_download() as download_info:
            print("click the download button")
            page.click(
                css_selector)

        download = download_info.value
        filepath = os.path.join('/app/db/ticktick', download.suggested_filename)
        download.save_as(filepath)
        print(f"Downloaded to: {filepath}")
    else:
        print('DRY RUN - NOT DOWNLOADING ANY FILES.')


def automate_task_export():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        page = browser.new_page()
        login(page)
        print("click on top-left 'account' image")
        page.click(r'img.w-\[32px\]')
        print("select 'settings' from the dropdown")
        page.click(
            r'li.dropdown-menu-menu-item:nth-child(1) > a:nth-child(1) > span:nth-child(2)')
        download_with_save(page, r'button.mr-\[16px\] > a:nth-child(1)')
        browser.close()


def automate_habit_export():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        page = browser.new_page()
        login(page)
        print("select habits icon from the sidebar")
        page.click('.icon-habit-sidebar')
        page.wait_for_timeout(1000)
        print("click 'more' (3 dots) icon from the top-right")
        page.click('svg.cursor-pointer')

        download_with_save(page, 'li.dropdown-menu-menu-item:nth-child(2) > a:nth-child(1) > span:nth-child(2)')
        browser.close()


if __name__ == "__main__":
    print('STARTING RUN')
    automate_task_export()
    automate_habit_export()
    print('RUN COMPLETED')
