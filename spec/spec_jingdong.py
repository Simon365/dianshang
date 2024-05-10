from base.base import *

# enter to jingdong lingquan
def jd_lingquan_enter(driver):
    while (not exist(find_element_by_name(driver,"领券"))):
        s_sleep()
    try:
        find_element_by_name(driver,"领券").click()
        m_sleep()
        print("进入京东领券成功！")
        return True
    except Exception as e:
        print(format(e))
        print("进入领券失败！")
        return False

# qiandaolingjiangli
def jd_sign_lingjiangli(driver):
    i = 0
    for i in range(10):
        print("try to take jiangli No." + str(i))
        find_element_by_name(driver, "签到领奖励").click()
        s_sleep()

# lingjingdou
def jd_sign_lingjingdou(driver):
    while (not exist(find_element_by_name(driver, "领京豆"))):
        s_sleep()
    try:
        print("开始京东领京豆！")
        find_element_by_name(driver, "领京豆").click()
        s_sleep()
        find_element_by_name(driver, "种豆得豆").click()
        s_sleep()
    except Exception as e:
        print(format(e))
        print("京东领京豆失败！")

# jingdong shouqu yingyangye
def jd_take_yingyangye(driver):
    swipedown(driver)
    i = 0
    for i in range (20):
        print("疯狂领京豆第"+str(i)+"次开始！")
        try:
            find_element_by_name(driver,"喊TA回来").click()
            s_sleep()
            find_element_by_name(driver, "点击收取").click()
            s_sleep()
        except Exception as e:
            print(format(e))
            print("帮人领京豆失败！")


