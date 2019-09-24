from FundApp import SitTester, SettingPage
from FundApp.flow.Steps import *
from FundApp.TestCase.conftest import testcase, debug_case
from common.utils.Driver import Driver, scroll
from FundApp.TestCase.conftest import BaseTest
import random
from common.ConfigeReader import ReadConfig
from common.RequestInterFace import setJwt,getJwt,postCreatOrd,OCRAuth



from common.DBExcue import SETHTFen


__dir__ = os.path.dirname(os.path.abspath(__file__))

configName = os.path.join(__dir__,"config.txt")

register_user = None

class TestSitSuite(BaseTest):
    @testcase(reruns=1)
    def test_01_sign_up(self, mobile=None):
        """  注册  """
        #点击麦芽首页消费分期
        #Driver.d.xpath('//*[@resource-id="com.maiyafenqi:id/product_rc"]/android.view.View[1]').click()
        #进入我的页面
        HomePage().click_mine_view()
        #点击立即登录
        Driver.d(resourceId="com.maiyafenqi:id/iv_login").click()
        time.sleep(0.5)
        #点击注册按钮 进入注册界面
        Driver.d(resourceId="com.maiyafenqi:id/register_tv").click()
        time.sleep(2)
        if mobile is None:
            mobile = create_iphone_no()
        sign_up_steps(Driver.d, mobile)
        time.sleep(1)
        #保存手机号码
        ReadConfig().setResData(option="mobile",value=mobile)
    @testcase(reruns=1)
    def test_02_login(self):
        """  登录  """
        HomePage().click_mine_view()
        #点击立即登录
        Driver.d(resourceId="com.maiyafenqi:id/iv_login").click()
        time.sleep(0.5)
        #输入手机号
        mobile = ReadConfig().getResData("mobile")
        Driver.d(resourceId="com.maiyafenqi:id/phone_et").set_text("{}".format(mobile))
        time.sleep(0.5)
        #输入密码
        Driver.d(resourceId="com.maiyafenqi:id/password_et").set_text("it789123")
        time.sleep(0.5)
        # 收起软键盘
        Driver.d.long_click(0.925, 0.517, 1)
        time.sleep(1)
        #点击登录按钮
        Driver.d(resourceId="com.maiyafenqi:id/login_tv").click()
        time.sleep(1)

    @testcase(reruns=1)
    def test_03_createOrd(self):
        """  创建订单  """
        #获取手机号
        mobile = ReadConfig().getResData("mobile")
        #调用登录接口，更新存储jwt到配置
        setJwt("login_params",["loginName","blackBox"],[mobile,mobile])
        #调用创建订单接口 创建订单
        postCreatOrd()
        #进入首页
        HomePage().firstpage_view.click()
        #刷新获取订单信息
        Driver.d.swipe(0.49, 0.255,0.501, 0.442)

    @testcase(reruns=1)
    def test_04_ocr(self, amount=None):
        """  OCR认证  """
        #进入首页
        HomePage().firstpage_view.click()

        #调用接口进行实名认证
        OCRAuth()
        #点击继续填写
        Driver.d(resourceId="com.maiyafenqi:id/actionTV").click_exists(timeout=1)
    @testcase(reruns=1)
    def test_05_PersonInfo(self):
        """完善个人信息"""
        # #进入首页
        # HomePage().firstpage_view.click()
        #点击继续填写
        Driver.d(resourceId="com.maiyafenqi:id/actionTV").click_exists(timeout=1)
        #进入个人信息界面
        #选择婚姻状况
        Driver.d.xpath('//*[@resource-id="com.maiyafenqi:id/marriage_item"]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]').click(timeout=1)
        #滑动选择
        Driver.d.swipe(0.584, 0.878,0.582, 0.847)
        #点击确定按钮：
        Driver.d(resourceId="com.maiyafenqi:id/btnSubmit").click_exists(timeout=1)
        #x选择文化程度列表
        Driver.d.xpath('//*[@resource-id="com.maiyafenqi:id/education_item"]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]').click()
        #滑动选择
        Driver.d.swipe(0.47, 0.885,0.492, 0.774)
        #点击确认按钮
        Driver.d(resourceId="com.maiyafenqi:id/btnSubmit").click_exists(timeout=1)
        #点击选择收入水平
        Driver.d.xpath('//*[@resource-id="com.maiyafenqi:id/income_item"]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]').click()
        #滑动选择
        Driver.d.swipe(0.47, 0.885,0.492, 0.774)
        #点击选择确认按钮
        Driver.d(resourceId="com.maiyafenqi:id/btnSubmit").click_exists(timeout=1)
        #输入公司名称
        Driver.d(resourceId="com.maiyafenqi:id/input_et", text="请填写您的公司名称").set_text("JD科技")
        time.sleep(1)
        # 收起软键盘
        Driver.d.long_click(0.925, 0.517, 1)
        #输入职位信息
        Driver.d(resourceId="com.maiyafenqi:id/input_et", text="请填写您的职位名称").set_text("Python开发工程师")
        # 收起软键盘
        Driver.d.long_click(0.925, 0.517, 1)
        #点击选择所在城市
        Driver.d.xpath('//*[@resource-id="com.maiyafenqi:id/company_city_item"]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]').click()
        time.sleep(1)
        #滑动选择
        Driver.d.swipe(0.47, 0.885,0.492, 0.774)
        time.sleep(1)
        #点击确认按钮
        Driver.d(resourceId="com.maiyafenqi:id/btnSubmit").click_exists(timeout=1)
        time.sleep(1)
        #设置公司地址
        Driver.d(resourceId="com.maiyafenqi:id/input_et", text="请填写您的公司地址").set_text("浦东新区")
        time.sleep(1)
        # 收起软键盘
        Driver.d.long_click(0.925, 0.517, 1)
        #滑动屏幕，将隐藏的区域显示出来
        Driver.d.swipe(0.402, 0.837,0.402, 0.616)
        time.sleep(1)
        #滑动屏幕，将隐藏的区域显示出来
        Driver.d.swipe(0.402, 0.837,0.402, 0.616)
        time.sleep(1)
        #滑动屏幕，将隐藏的区域显示出来
        Driver.d.swipe(0.402, 0.837,0.402, 0.616)
        time.sleep(1)
        #选择住房下拉框
        Driver.d.xpath('//*[@resource-id="com.maiyafenqi:id/housing_item"]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]').click()
        time.sleep(1)
        #滑动选择
        Driver.d.swipe(0.47, 0.885,0.492, 0.774)
        #点击确认按钮
        Driver.d(resourceId="com.maiyafenqi:id/btnSubmit").click_exists(timeout=1)
        time.sleep(1)
        #点击选择所在城市 下拉框
        Driver.d.xpath('//*[@resource-id="com.maiyafenqi:id/housing_city_item"]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]').click()
        time.sleep(1)
        # 滑动选择
        Driver.d.swipe(0.47, 0.885, 0.492, 0.774)
        #点击确认按钮
        Driver.d(resourceId="com.maiyafenqi:id/btnSubmit").click_exists(timeout=1)
        #设置家庭住址
        Driver.d(resourceId="com.maiyafenqi:id/input_et", text="请填写您的家庭地址").set_text("浦东新区，塘桥")
        time.sleep(1)
        # 收起软键盘
        Driver.d.long_click(0.925, 0.517, 1)
        #设置电子邮箱地址
        Driver.d(resourceId="com.maiyafenqi:id/input_et", text="请填写您的邮箱地址").set_text("530696867@qq.com")
        time.sleep(1)
        # 收起软键盘
        Driver.d.long_click(0.925, 0.517, 1)
        #点击"下一步"按钮
        Driver.d(resourceId="com.maiyafenqi:id/next_tv").click_exists(timeout=1)
    @testcase(reruns=2)
    def test_06_invest_MailList(self):
        """  通讯录认证  """
        #点击继续填写
        Driver.d(resourceId="com.maiyafenqi:id/actionTV").click_exists(timeout=1)
        #进入通讯录认证
        Driver.d(resourceId="com.maiyafenqi:id/back_iv").click()
        time.sleep(1)
        #点击授权，如果有的话点击
        Driver.d.click(0.277, 0.685)
        time.sleep(1)
        #选择通讯录中的人员
        Driver.d.xpath('//*[@resource-id="android:id/list"]/android.view.View[3]').click()
        time.sleep(1)
        #选择联系人关系
        Driver.d(resourceId="com.maiyafenqi:id/select_iv").click()
        time.sleep(1)
        # 滑动选择
        Driver.d.swipe(0.47, 0.885, 0.492, 0.774)
        #点击确认按钮
        Driver.d(resourceId="com.maiyafenqi:id/btnSubmit").click_exists(timeout=1)
        time.sleep(1)
        #点击选择通讯录按钮
        Driver.d(resourceId="com.maiyafenqi:id/other_contact_iv").click_exists(timeout=1)
        time.sleep(1)
        #点击授权，如果有的话点击
        Driver.d.click(0.277, 0.685)
        time.sleep(1)
        # # 滑动选择
        # Driver.d.swipe(0.47, 0.885, 0.492, 0.774)
        #选择通讯录中的人员
        Driver.d.xpath('//*[@resource-id="android:id/list"]/android.view.View[6]').click()
        time.sleep(1)
        #点击下一步按钮
        Driver.d(resourceId="com.maiyafenqi:id/next_tv").click()

    @testcase(reruns=1)
    def test_07_Auth(self):
        """  认证授权  """
        #点击继续填写
        Driver.d(resourceId="com.maiyafenqi:id/actionTV").click_exists(timeout=1)
        time.sleep(1)
        Driver.d(resourceId="com.maiyafenqi:id/next_tv").click()
        time.sleep(1)
    @testcase(reruns=1)
    def test_08_moveFile(self):
        """  上传影响资料  """
        #点击继续填写
        Driver.d(resourceId="com.maiyafenqi:id/actionTV").click_exists(timeout=1)
        time.sleep(1)

        #点击手术确认书按钮
        Driver.d.xpath('//*[@resource-id="com.maiyafenqi:id/auth_info_RV"]/android.view.View[1]/android.widget.ImageView[1]').click()
        time.sleep(1)
        #点击屏幕
        Driver.d.click(0.179, 0.2)
        time.sleep(1)
        #点击屏幕
        Driver.d.click(0.179, 0.2)
        time.sleep(2)

        # 点击芝麻信用分截图
        Driver.d.xpath('//*[@resource-id="com.maiyafenqi:id/auth_info_RV"]/android.view.View[2]/android.widget.ImageView[1]').click()
        time.sleep(1)
        # 点击屏幕
        Driver.d.click(0.179, 0.2)
        time.sleep(1)
        # 点击屏幕
        Driver.d.click(0.179, 0.2)
        time.sleep(1)


        #点击手机运营商实名截图
        Driver.d.xpath('//*[@resource-id="com.maiyafenqi:id/auth_info_RV"]/android.view.View[3]/android.widget.ImageView[1]').click()
        time.sleep(1)
        #点击屏幕
        Driver.d.click(0.179, 0.2)
        time.sleep(1)
        #点击屏幕
        Driver.d.click(0.179, 0.2)
        time.sleep(1)
        #点击手机运营商在网时长（网龄）截图"
        Driver.d.xpath('//*[@resource-id="com.maiyafenqi:id/auth_info_RV"]/android.view.View[4]/android.widget.ImageView[1]').click()
        time.sleep(1)
        #点击屏幕
        Driver.d.click(0.179, 0.2)
        time.sleep(1)
        #点击屏幕
        Driver.d.click(0.179, 0.2)
        time.sleep(1)

        # 点击芝麻信用分截图
        Driver.d.xpath('//*[@resource-id="com.maiyafenqi:id/auth_info_RV"]/android.view.View[2]/android.widget.ImageView[1]').click()
        time.sleep(1)
        # 点击屏幕
        Driver.d.click(0.179, 0.2)
        time.sleep(1)
        # 点击屏幕
        Driver.d.click(0.179, 0.2)
        time.sleep(1)

        #点击下一步按钮
        Driver.d(resourceId="com.maiyafenqi:id/next_tv").click()
        time.sleep(1)
    @testcase(reruns=1)
    def test_09_FaceAuth(self):
        """  人脸识别-Sql修改  """
        #点击返回按钮
        Driver.d(resourceId="com.maiyafenqi:id/title_left_icon").click_exists(timeout=1)
        #设置活体分
        SETHTFen()
        #点击继续填写
        Driver.d(resourceId="com.maiyafenqi:id/actionTV").click_exists(timeout=1)
        time.sleep(1)

    @testcase(reruns=1)
    def test_10_confirm(self, username=None):
        """  确认借款  """
        # 点击继续填写
        Driver.d(resourceId="com.maiyafenqi:id/actionTV").click_exists(timeout=1)
        time.sleep(1)
        #勾选我已阅读并同意签署《非在校学生承诺函》
        Driver.d(resourceId="com.maiyafenqi:id/agreement_iv").click()
        time.sleep(1)
        #点击确认按钮
        Driver.d(resourceId="com.maiyafenqi:id/confirm_tv").click()
        time.sleep(2)
        #点击确认按钮
        Driver.d(resourceId="com.maiyafenqi:id/btn_confirm").click()
        time.sleep(1)
        # if username is None:
        #     username = register_user
        # login(Driver.d, username)
        # Driver.d(text=u"跳过").click_exists(timeout=2)
        # print("登录成功")
        # Driver.d(text=u"先去逛逛").click_exists(timeout=3)


if __name__ == "__main__":
    pass



