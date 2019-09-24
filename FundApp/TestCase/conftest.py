import time
from FundApp.flow.Steps import reset_and_start_nonoapp,set_env
from functools import wraps
from common.utils.Driver import Driver
from unittest import TestCase
import re
from FundApp.flow.Steps import start_nonoapp
import subprocess


class BaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        """启动app 并选择环境"""
        reset_and_start_nonoapp(Driver.d)
        set_env(Driver.d)
        time.sleep(2)
        Driver.d.swipe(0.87, 0.664,	0.24, 0.669)
        time.sleep(2)
        Driver.d.swipe(0.87, 0.664,	0.24, 0.669)
        time.sleep(2)
        Driver.d.swipe(0.87, 0.664,	0.24, 0.669)
        time.sleep(2)
        Driver.d.swipe(0.87, 0.664,	0.24, 0.669)
        time.sleep(2)
        Driver.d.swipe(0.87, 0.664,	0.24, 0.669)
        time.sleep(2)
        #点击滑动"跳过"按钮
        Driver.d(resourceId="com.maiyafenqi:id/guide_tv").click()

    def setUp(self):
        #有X的先点掉
        Driver.d(resourceId="com.maiyafenqi:id/close_iv").click_exists(timeout=2)
        #有返回<按钮先点掉
        Driver.d(resourceId="com.maiyafenqi:id/title_left_icon").click_exists(timeout=2)
        # 进入首页
        Driver.d(resourceId="com.maiyafenqi:id/tab_text_tv", text="首页").click_exists(timeout=2)
        # """ loading等待 循环检测 """
        # for i in range(0, 10):
        #     if Driver.d(resourceId="com.nonoapp:id/progress_image").exists:
        #         time.sleep(3)
        #     else:
        #         break

    def tearDown(self):
        subprocess.Popen('ps -ef | grep \'chromedriver\' | grep -v \'grep\' | awk \'{print $2}\' | xargs kill -9',
                         shell=True)

    @classmethod
    def tearDownClass(cls):
        subprocess.Popen('ps -ef | grep \'chromedriver\' | grep -v \'grep\' | awk \'{print $2}\' | xargs kill -9',
                         shell=True)
        #Driver.d.app_stop('com.maiyafenqi')


def testcase(reruns: int, exceptions=Exception):
    '''

    :param exceptions:
    :param reruns:
    :return:
    '''
    def decorator(func):# test_01_sign_up(self, username=None):
        @wraps(func)#test_01_sign_up
        def wrapper(*args, **kwargs):
            module = __import__('FundApp.TestCase', fromlist=['TestCase'])
            print("-------module-------",module)
            classname = func.__qualname__.split('.')[0]
            print("-------classname-------",classname)
            cls = getattr(module,classname)
            total = reruns
            while total>=0:
                try:
                    date = time.strftime('%Y%m%d-%H%M%S', time.localtime())
                    ret = func(*args, **kwargs)
                    name = func.__qualname__ + date + "SUCCESS" + '.PNG'
                    Driver.screenshot(name)
                    return ret
                except exceptions as e:
                    date = time.strftime('%Y%m%d-%H%M%S', time.localtime())
                    name = func.__qualname__ + date + "FAILED" + '.PNG'
                    Driver.screenshot(name)
                    if total == 0:
                        raise e
                    total -= 1
                    time.sleep(1)
                    print("failed,try again....\n failed reason:\n{}".format(e))
                    cls().setUp()
        return wrapper
    return decorator


def debug_case(*args: int):
    func_list = []
    self  = None
    module = __import__('__main__')
    for item in dir(module):
        cls = getattr(module, item)
        if isinstance(cls,type) and issubclass(cls,TestCase):
            self = cls()
            for item in dir(self):
                func = getattr(self,item)
                if item.startswith('test') and hasattr(func,'__call__'):
                    func_list.append(func)
    if args:
        args = list(map(lambda x: str(x)if x >= 10 else "0"+str(x), sorted(args)))
        #func命名格式test_01_...
        test_func_list = [func for func in func_list if re.search('(\d+)', func.__name__).group(1) in args]
    else:
        test_func_list = func_list
    first_test = re.search('(\d+)', test_func_list[0].__name__).group(1)
    setUpClass = getattr(self,'setUpClass',None)
    setUp = getattr(self, 'setUp',None)
    tearDown = getattr(self, 'tearDown',None)
    tearDownClass = getattr(self, 'tearDownClass',None)
    if first_test in ['01','1'] and setUpClass is not None:
        setUpClass()
    for func in test_func_list:
        if setUp is not None:
            setUp()
            print('test :-->{}'.format(func.__name__))
            func()
        if tearDown is not None:
            tearDown()
    if tearDownClass is not None:
        tearDownClass()


def before_test():
    '''
    1.安装App
    2.设置测试环境
    3.watcher()
    :return:
    '''


if __name__ == "__main__":
    pass