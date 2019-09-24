import unittest
from FundApp.TestCase.test_sit import TestSitSuite
from FundApp.TestCase.test_sit_main import TestSitMain
from FundApp.TestCase.test_sit_static import TestSitStatic


USER_SUITE = unittest.TestLoader().loadTestsFromTestCase(TestSitSuite)
#MAIN_SUITE = unittest.TestLoader().loadTestsFromTestCase(TestSitMain)
# STATIC_SUITE = unittest.TestLoader().loadTestsFromTestCase(TestSitStatic)
SIT_SUITE = unittest.TestSuite()
# SIT_SUITE.addTests([USER_SUITE, MAIN_SUITE, STATIC_SUITE])
SIT_SUITE.addTest(USER_SUITE)


if __name__ == "__main__":
    pass

