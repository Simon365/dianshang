from spec.spec import *

# pdd签到提现
def pdd_sign_module(driver):
    pdd_kill_home_ad(driver)
    if (pdd_sign_enter(driver)):
        pdd_sign_now(driver)

