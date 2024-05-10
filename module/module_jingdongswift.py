from spec.spec import *

# 签到提现
def jd_sign_cash_module(driver):
    print("准备开始......")
    jd_swift_close_popup_page_1(driver)
    jd_swift_sign_cash(driver)

# facaidayingjia
def jd_facaidayingjia_module(driver):
    print("发财大赢家开始......")
    jd_swift_back(driver)
    s_sleep()
    if(jd_swift_enter_facaidayingjia(driver)):
        print("领取发财红包......")
        jd_swift_facai_red_bag(driver)

# 领红包
def jd_receive_red_envelope_module(driver):
    print("领红包开始......")
    jd_swift_back(driver)
    s_sleep()
    if (jd_swift_enter_lingredpackage(driver)):
        jd_swift_linghongbao(driver)
        jd_swift_browse_linghongbao(driver)

# 好看，看视频
def jd_watch_microvideo_module(driver):
    print("浏览视频开始......")
    jd_swift_back(driver)
    s_sleep()
    if (jd_swift_enter_microvideo(driver)):
        jd_swift_browse_micro_vedo(driver)


