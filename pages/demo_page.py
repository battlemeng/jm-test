class Links():
    # link_templates = 1111

    def __init__(self, page):
        self.page = page

    @property
    def q(self):
        return self.page.goto("https://baidu.com")

    @property
    def w(self):
        return self.page.get_by_role("menuitem", name="搜索点击").locator("div").click()

    @property
    def e(self):
        return self.page.get_by_role("menuitem", name="页面").click()

    @property
    def r(self):
        return self.page.get_by_role("button", name="导入").click()
