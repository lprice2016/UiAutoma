from common.utils.Driver import Driver
import time


class HomePage:
    @property
    def mine_view(self):
        return Driver.d(resourceId="com.maiyafenqi:id/tab_text_tv", text="我的")

    @property
    def Dingdan(self):
        return Driver.d(resourceId="com.maiyafenqi:id/tab_text_tv", text="订单")
    @property
    def firstpage_view(self):
        return Driver.d(resourceId="com.maiyafenqi:id/tab_text_tv", text="首页")

    def click_mine_view(self):
        self.mine_view.click()
        time.sleep(4)
