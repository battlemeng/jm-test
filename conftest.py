import os
from pathlib import Path
import pytest
from playwright.sync_api import Page
from slugify import slugify

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    print('browser  '+os.getcwd())
    return {
        **browser_type_launch_args,
        "headless": False
    }

@pytest.fixture(scope="session", autouse=True)
def unified_login(browser)-> None:
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://login.baidu.com")
    page.get_by_placeholder("账号").click()
    page.get_by_placeholder("账号").fill("zhanghao")
    page.get_by_placeholder("密码").click()
    page.get_by_placeholder("密码").fill("passwd")
    page.get_by_role("button", name="登录").click()
    page.wait_for_timeout(3000)
    context.storage_state(path="state.json")
    print("1   "+os.getcwd())
    # page.close()
    # context.close()

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):

    print('2 '+os.getcwd())
    return {
        **browser_context_args,
        "ignore_https_errors":True,
        "storage_state":"state.json",
        "viewport": {"width":1920,"height":1080}

    }
