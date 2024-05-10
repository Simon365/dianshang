from base.base import *

# pdd swift back
def pdd_back(driver):
    while (not exist(find_element_by_name(driver,"签到"))):
        driver.back()
        m_sleep()

# pdd kill home ad
def pdd_kill_home_ad(driver):
    try:
        if exist(find_element_by_name(driver,"可能认识的好友")):
            driver.find_element_by_android_uiautomator(
                'new UiSelector().resourceId("com.xunmeng.pinduoduo:id/pdd").index(0)').click()
            s_sleep()
        else:
            print("拼多多首页没有找到弹出式广告！")
    except Exception as e:
        print(format(e))
        print("拼多多首页关闭弹出式广告失败！")

    try:
        if exist(find_element_by_id(driver, "com.android.packageinstaller:id/permission_allow_button")):
            find_element_by_id(driver, "com.android.packageinstaller:id/permission_allow_button").click()
            s_sleep()
            print("等待返回拼多多首页！")
            pdd_back(driver)
    except Exception as e:
        print(format(e))
        print("允许拼多多获取信息！")

# pdd sign
def pdd_sign_enter(driver):
    while (not exist(find_element_by_name(driver,"签到"))):
        s_sleep()
    try:
        print("查找拼多多签到入口并签到！")
        find_element_by_name(driver,"签到").click()
        m_sleep()
        return True
    except Exception as e:
        print(format(e))
        print("进入拼多多签到模块失败！")
        return False

# click the "lijiqiandao" button
def pdd_nowsign_button(driver):
    try:
        print("点击立即签到按钮......")
        find_element_by_name(driver, "立即签到").click()
        s_sleep()
    except Exception as e:
        print(format(e))
        print("没有立即签到按钮！")

def pdd_sign_now(driver):
    try:
        print("立即拼多多签到开红包")
        find_element_by_name(driver,"立即签到开红包").click()
        m_sleep()

    except Exception as e:
        print(format(e))
        print("拼多多立即签到开红包失败！")

    if exist(find_element_by_name(driver, "去领更多红包")):
        try:
            print("拼多多去领更多红包......")
            find_element_by_name(driver, "去领更多红包").click()
            m_sleep()
            pdd_nowsign_button(driver)
        except Exception as e:
            print(format(e))
            print("拼多多去领更多红包失败！")
    if exist(find_element_by_name(driver, "去领更多红包")):
        try:
            print("拼多多去领更多红包")
            driver.find_element_by_android_uiautomator\
                ('new UiSelector().text("50").index(0).clickable(true)').click()
            m_sleep()
        except Exception as e:
            print(format(e))

    if exist(find_element_by_name(driver, "下单得现金红包")):
        try:
            print("拼多多下单得现金红包")
            find_element_by_name(driver, "下单得现金红包").click()
            m_sleep()
        except Exception as e:
            print(format(e))
            print("拼多多进入下单得现金红包页面失败！")

    if exist(find_element_by_name(driver, "下单得现金红包")):
        try:
            print("pdd下单得现金红包")
            driver.find_element_by_android_uiautomator \
                ('new UiSelector().text("50").index(0).clickable(true)').click()
            m_sleep()
        except Exception as e:
            print(format(e))

    if exist(find_element_by_name(driver, "去领更多红包")):
        try:
            print("拼多多去领更多红包")
            driver.find_element_by_android_uiautomator \
                ('new UiSelector().index(3).clickable(true)').click()
            m_sleep()
        except Exception as e:
            print(format(e))
            print("拼多多去领更多红包失败！")

    if exist(find_element_by_name(driver, "做任务领红包")):
        print("拼多多做任务领红包")
        try:
            driver.find_element_by_android_uiautomator \
               ('new UiSelector().text("立即领取").index(0).clickable(false)').click()
            s_sleep()
        except Exception as e:
            print(format(e))
            print("拼多多做任务领红包失败！")


    if exist(find_element_by_name(driver, "做任务领红包")):
        print("拼多多做任务领红包")
        try:
            find_element_by_name(driver, "立即领取").click()
            s_sleep()
        except Exception as e:
            print(format(e))
            print("拼多多做任务领红包失败！")

    if exist(find_element_by_name(driver, "去开红包")):
        try:
            find_element_by_name(driver, "去开红包").click()
            s_sleep()
        except Exception as e:
            print(format(e))

    if exist(find_element_by_name(driver, "立即开红包")):
        try:
            find_element_by_name(driver, "立即开红包").click()
            s_sleep()
        except Exception as e:
            print(format(e))
            print("拼多多立即开红包失败！")

    if exist(find_element_by_name(driver, "逛街再得1个红包")):
        find_element_by_name(driver, "逛街再得1个红包").click()
        m_sleep()

    if exist(find_element_by_name(driver, "去领更多红包")):
        try:
            print("拼多多去领更多红包")
            driver.find_element_by_android_uiautomator \
                ('new UiSelector().index(3).clickable(true)').click()
            m_sleep()
        except Exception as e:
            print(format(e))
            print("拼多多去领更多红包失败！")

    if exist(find_element_by_name(driver, "去完成")):
        print("拼多多逛街领红包")
        try:
            find_element_by_name(driver, "去完成").click()
            s_sleep()
            i = 0
            for i in range (5):
                swipedown(driver)
                s_sleep()
        except Exception as e:
            print(format(e))
            print("拼多多逛街领红包失败！")


