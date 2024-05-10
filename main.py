import unittest

from module.module import *

deviceid_1 = 'Y5G69H69BYYHMBQG'
deviceid_2 = '127.0.0.1:62025'
deviceid_3 = '127.0.0.1:62001'
deviceid_4 = '66J5T18B02020990'
deviceid_5 = 'R3CM903NL1P'


class TestOther(unittest.TestCase):
    # initialize the device
    def setUp(self):
        global deviceid_1
        global deviceid_2
        global deviceid_3
        global deviceid_4
        global deviceid_5
        ver_dev4 = '10.0'
        ver_dev5 = '11'
        peer_SetUp(self, deviceid_4, ver_dev4)

    def test_case(self):
        driver = self.driver

        # driver.keyevent(3)
        # s_sleep()
        # if (launch_specific_app(driver, "京东极速版")):
        #     print("京东极速版启动成功！")
        #     jd_swift_close_infonotice(driver)
        #     jd_sign_cash_module(driver)
        #     jd_receive_red_envelope_module(driver)
        #     jd_watch_microvideo_module(driver)
        #
        # # jingdong
        # driver.keyevent(3)
        # s_sleep()
        # if (launch_specific_app(driver, "京东")):
        #     jd_lingquan_module(driver)
        #     jd_lingjingdou_module(driver)
        #
        # # pdd
        # driver.keyevent(3)
        # s_sleep()
        # if (launch_specific_app(driver, "拼多多")):
        #     print("拼多多启动成功！")
        #     m_sleep()
        #     pdd_sign_module(driver)

        # quick hand
        # driver.keyevent(3)
        # s_sleep()
        # if launch_specific_app(driver, "快手极速版"):
        #     print("快手极速版启动成功！")
        #     m_sleep()
        #     qh_browse_video_module(driver, 500)
        #     qh_browse_ad_video(driver, 10)
        #     qh_browse_zhibo_video(driver, 10)
        qh_browse_video_module(driver, 1000)

        # driver.keyevent(3)
        # s_sleep()
        # find_element_by_name(driver,'美食与购物').click()
        # s_sleep()
        # find_element_by_name(driver,'拼多多').click()
        # m_sleep()
        # find_element_by_name(driver,'多多视频').click()
        # m_sleep()
        # qh_browse_video_module(driver, 500)

    def tearDown(self):
        print("test completed!")


if __name__ == '__main__':
    unittest.main()
