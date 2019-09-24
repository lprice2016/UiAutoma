# -*- coding: utf-8 -*-
from common.utils.Driver import Driver

class MockPage:

    @property
    def confirm_button_view(self):
        if Driver.d(description='确定').exists(timeout=3):
            return Driver.d(description='确定')
        else:
            return Driver.d(text='确定')