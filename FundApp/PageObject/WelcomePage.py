from common.utils.Driver import Driver


class WelcomePage:

    @property
    def button(self):
        e = Driver.d(resourceId="com.nonoapp:id/btn", text='立即注册领1888新手福利')
        if e.exists(timeout=3):
            return e
        return Driver.d(resourceId="com.nonoapp:id/btn", text='立即注册领5888特权本金')
