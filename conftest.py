import os
from pathlib import Path
import pytest
from playwright.sync_api import Page
from slugify import slugify

# conftest.py名称是pytest固定的配置脚本，不能改名称
# conftest.py文件不能被其他文件导入引用，只会被pytest用例编码（test_的测试文件方法）自动识别该文件以及调用，且不需要import导入
# pytest7.4版本前默认作用于当前目录和子目录  7.4版本后默认只作用于当前目录  可以通过参数修改作用域
# 因此同目录以及子目录的测试文件运行前都会预先执行conftest.py文件，相当于一个待启动状态
#    @1  写在conftest.py里的方法如果被测试用例里的方法（test_）开头引用（在测试编码运行之前作用，在测试编码时不起作用），那么会先运行conftest.py里的方法，（不满足才会在往上找对应的方法，相当于conftest是一个中间层，上层是其他方法，下层是测试用例编码，运行测试用例编码之前要调用外部先会调用conftest再调用上层其他方法，运行测试用例编码之时直接调用上层其他方法）
#    @2  如果没被调用就不会conftest.py里的方法执行，但如果加了autouse=True参数就会自动在作用域前自动调用（作用域的范围function<class<module<package<session）
# -function：每一个函数或方法都会调用
# -class：每一个类调用一次，一个类中可以有多个方法
# -module：每一个.py文件调用一次，该文件内又有多个function和class
# -session：总调用一次，可以跨.py文件调用，每个.py文件就是module





# playwright测试框架启动顺序，先启动playwright->brower(火狐，google等)->contest(上下文隔离，不同之间的contest不同享数据：个人等信息，相同之间同享数据，如：登录)->page（一个新页面）
# 因此在运行测试编码（test_）开头包含要创建的先启动page，会先调用playwright再调用brower再调用contest再调用page组件
#    在运行测试编码（test_）开头包含要创建的先启动contest，会先调用playwright再调用brower再调用contest 以此类推，包含调用哪一层都是依次调用
# 自定义夹具选项 browser
# 而browser_type.launch()相当于打开brower以及包含此层面的一些公共配置的设置，影响brower层面，映射contest以及page层
# browser_type_launch_args：覆盖browser_type.launch()的启动参数。它应该返回一个字典。因此修改此方法时相当于修改要打开的brower公共配置
# browser_type_launch_args写在conftest.py里，因此当测试用例编码（test_）在执行之前调用创建浏览器的话，相当于自动调用了此覆盖方法，对应@1

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    print('browser  '+os.getcwd())
    return {
        **browser_type_launch_args,
        "headless": False
    }

# 对应@2
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


# 自定义夹具选项 conftest
# 同理browser.new_context()相当于打开context以及包含此层面的一些公共配置的设置，影响context层面，映射page层
# browser_context_args：覆盖browser.new_context()的启动参数。它应该返回一个字典。因此修改此方法时相当于修改要打开的context公共配置
# browser_context_args写在conftest.py里，因此当测试用例编码（test_）在执行之前调用创建context的话，相当于自动调用了此覆盖方法，对应@1
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):

    print('2 '+os.getcwd())
    return {
        **browser_context_args,
        "ignore_https_errors":True,
        "storage_state":"state.json",
        "viewport": {"width":1920,"height":1080}

    }
