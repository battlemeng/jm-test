import os
import sys
from playwright.async_api import Page
from playwright.sync_api import expect
from pages.link_list_page import Links
from utils.download_jm import download_jm
from utils.read_data import get_data_links


def test_example(page: Page) -> None:
    dud = Links(page)
    dud.q
    dud.w
    dud.e
    dud.r
    # page.pause()
    download_jm(page, get_data_links('download_path'), "下载模板")
