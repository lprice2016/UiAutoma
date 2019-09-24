# -*- coding: utf-8 -*-
from __future__ import print_function
from common.utils.Driver import Driver

class OpenAccountPage:

    @property
    def real_name_view(self):
        return Driver.d(resourceId='realname')

    @property
    def open_account_bank_view(self):
        return Driver.d(description=u"开户行")

    @property
    def user_mobile_view(self):
        return Driver.d(resourceId='mobile')

    @property
    def next_button_view(self):
        return Driver.d(resourceId="btn_next")