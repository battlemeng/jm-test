import os
import re

import pytest
from playwright.sync_api import Page, expect


def test_example(page) -> None:
    print(os.getcwd()+ '   bendi')
  
    page.goto("https://baidu.com")
    # page.locator("label").filter(has_text="测试项目").locator("span").nth(1).click()
    # page.get_by_placeholder("请输入项目编码/名称").click()
    # page.get_by_placeholder("请输入项目编码/名称").fill("test")
    # page.get_by_role("button").nth(1).click()
    # expect(page.locator("tbody")).to_contain_text("T022035")
    # expect(page.locator("tbody")).to_contain_text("UItestJm")
    # page.get_by_text("UItestJm").click()
    page.pause()
    page.get_by_role("menuitem", name="调测&验收").get_by_role("img").nth(1).click()
    page.get_by_role("menuitem", name="微波链路列表").click()
    page.get_by_role("button", name="新增").click()
    page.get_by_placeholder("请输入链路名称").click()
    page.get_by_placeholder("请输入链路名称").fill("11-22")
    page.get_by_label("站点1名称(ID)").click()
    page.get_by_label("站点1名称(ID)").fill("1-1")
    page.get_by_label("站点2名称(ID)").click()
    page.get_by_label("站点2名称(ID)").fill("2-2")
    page.get_by_role("button", name="确定").click()
    expect(page.locator("a")).to_contain_text("11-22")
    page.get_by_role("row", name="11-22 编辑 初始状态 1-1 初始状态 2024-").locator("label span").nth(1).click()
    page.get_by_role("button", name="删除").click()
    page.get_by_role("button", name="确定").click()
    page.get_by_role("button", name="确定").click()
