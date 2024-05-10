from spec.spec import *

# jingdong lingquan
def jd_lingquan_module(driver):
    if (jd_lingquan_enter(driver)):
        print("enter jingdong lingquan success!")
        jd_sign_lingjiangli(driver)


# jingdong lingjindou
def jd_lingjingdou_module(driver):
    jd_sign_lingjingdou(driver)
    jd_take_yingyangye(driver)

