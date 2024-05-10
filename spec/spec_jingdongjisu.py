from base.base import *

def jd_swift_close_infonotice(driver):
    print("正在关闭开启消息通知请求......")
    try:
        find_element_by_id(driver, "com.jd.jdlite:id/iv_close_install").click()
        s_sleep()
    except Exception as e:
        print(format(e))
        print("没有发现开启消息通知弹框！")


def jd_swift_close_popup_page_1(driver):
    print("正在关闭弹出广告页面......")
    try:
        find_element_by_content_desc(driver, "关闭页面").click()
        m_sleep()
    except Exception as e:
        print(format(e))
        print("没有找到弹出广告！")

def jd_swift_sign_cash(driver):
    print("开始签到提现......")
    while (not exist(find_element_by_name(driver, "签到提现"))):
        s_sleep()
    try:
        find_element_by_name(driver, "签到提现").click()
        m_sleep()
        while(not exist(find_element_by_name(driver, "我的奖励"))):
            s_sleep()
        print("京东签到提现成功！")
    except Exception as e:
        print(format(e))
        print("没有找到签到提现入口！")

def jd_swift_enter_lingredpackage(driver):
    while (not exist(find_element_by_name(driver, "领红包"))):
        s_sleep()
    try:
        find_element_by_name(driver, "领红包").click()
        m_sleep()
        while(not exist(find_element_by_name(driver, "活动规则"))):
            s_sleep()
        return True
    except Exception as e:
        print(format(e))

def jd_swift_linghongbao(driver):
    try:
        if exist(find_element_by_name(driver, "bag_btn_open")):
            find_element_by_name(driver, "bag_btn_open").click()
            m_sleep()
            print("京东极速版领红包成功！")
        else:
            driver.back()
    except Exception as e:
        print(format(e))

    i = 0
    for i in range(3):
        try:
            if exist(find_element_by_name(driver, "bag_btn_goon")):
                find_element_by_name(driver, "bag_btn_goon").click()
                m_sleep()
                print("京东极速版继续领红包成功！")

        except Exception as e:
            print(format(e))

    try:
        if exist(find_element_by_name(driver, "bag_btn_no")):
            print("红包已经领完了!")
            s_sleep()
    except Exception as e:
        print(format(e))

def jd_swift_browse_linghongbao(driver):
    i = 0
    print("查看是否有浏览送积分活动......")
    if exist(find_element_by_id(driver, 'com.jd.jdlite:id/pro_fl')):
        for i in range(20) :
            print("京东浏览送积分向下翻页开始......")
            while (not exist(find_element_by_name(driver, "点击逛下一个")) and (not exist(find_element_by_name(driver, "今日已完成")))):
                swipedown(driver)
                s_sleep()
                # try:
                #     print("尝试关闭弹框！")
                #     driver.find_element_by_android_uiautomator(
                #     'new UiSelector().index(2).clickable(true)').click()
                # except Exception as e:
                #     print("没有找到弹出框关闭按钮！")
                #     print(format(e))
                if exist(find_element_by_name(driver, "今日已完成")):
                    return

            if exist(find_element_by_name(driver, "今日已完成")):
                print("京东极速版视频浏览今日已完成！")
                return
            else:
                try:
                    find_element_by_name(driver, "点击逛下一个").click()
                    m_sleep()
                except Exception as e:
                    print(format(e))
                    print("京东极速版视频浏览今日已完成！")

def jd_swift_enter_facaidayingjia(driver):
    while (not exist()):
        s_sleep()
    try:
        find_element_by_name(driver, "发财大赢家").click()
        m_sleep()
        return True
    except Exception as e:
        print(format(e))

def jd_swift_facai_red_bag(driver):
    if exist(find_element_by_index(driver,'15')):
        print("接着找按钮......")
        try:
            el = find_element_by_index(find_element_by_index(driver,'15'), '2')
            el.click()
            m_sleep()
            if (exist(find_element_by_name("开红包"))):
                find_element_by_name("开红包").click()
                m_sleep()
                # 收下红包
                if exist(find_element_by_name("点击收下")):
                    find_element_by_name("点击收下").click()
                    m_sleep()
                    # 继续领红包
                    ele = find_element_by_index(find_element_by_index(driver, '15'), '2')
                    ele.click()
                    m_sleep()
                    # 红包领完后关闭弹窗
                    try:
                        ele = driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.Image").clickable(true)')
                        ele.click()
                    except Exception as e:
                        print(format(e))
                else:
                    # 处理没有领到红包
                    ele = find_element_by_index(find_element_by_index(driver, '15'), '2')
                    ele.click()
                    m_sleep()
                    try:
                        ele = driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.Image").clickable(true)')
                        ele.click()
                    except Exception as e:
                        print(format(e))

            # i = 0
            # for i in range(5):
            #     el.click()
            #     m_sleep()
            #     i = i + 1
            #     if (exist(find_element_by_name("开红包"))):
            #         find_element_by_name("开红包").click()

        except Exception as e:
            print(format(e))
    else:
        print("没有找到领红包按钮！")

    print("开始逛好物......")
    try:
        ele = driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.ListView").index(6)')
        find_element_by_index(ele, '2').click()
        m_sleep()
        j = 0
        for j in range(4):
            find_element_by_name(driver, "去浏览").click()
            m_sleep()
            i = 0
            for i in range(5):
                swipedown(driver)
                s_sleep()
                # 关闭弹出广告
                try:
                    find_element_by_name(driver,"javascript:void(0);").click()
                except Exception as e:
                    print(format(e))
            driver.back()
            s_sleep()
        # 关闭浏览4个会场，领红包
        try:
            find_element_by_name(driver,"rb618-close").click()
            s_sleep()
        except Exception as e:
            print(format(e))

        if exist(find_element_by_name(driver,"点击收下")):
            find_element_by_name(driver,"点击收下").click()
            m_sleep()

    except Exception as e:
        print(format(e))

# 进入视频频道
def jd_swift_enter_microvideo(driver):
    while (not exist(find_element_by_content_desc(driver, "看看"))):
        s_sleep()
    try:
        find_element_by_content_desc(driver, "看看").click()
        m_sleep()
        # 关闭弹出广告
        try:
            find_element_by_id(driver, "com.jd.jdlite:id/close").click()
        except Exception as e:
            print(format(e))
        try:
            find_element_by_content_desc(driver, "关闭页面")
        except Exception as e:
            print(format(e))
        print("成功进入京东视频!")
        return True
    except Exception as e:
        print(format(e))

# browse video
def jd_swift_browse_micro_vedo(driver):
    print("开始浏览视频......")
    m_sleep()
    i = 0
    while not exist(find_element_by_name(driver, "今日已完成")):
        # 关闭弹出广告
        try:
            find_element_by_id(driver, "com.jd.jdlite:id/close").click()
        except Exception as e:
            print(format(e))
        try:
            find_element_by_content_desc(driver, "关闭页面")
        except Exception as e:
            print(format(e))
        print("现在开始播放京东极速版第 " + str(i) + " 个视频......")
        swipedown(driver)
        m_sleep()
        i = i + 1
        if exist(find_element_by_name(driver, "今日已完成")):
            return

# jingdong swift back
def jd_swift_back(driver):
    while not exist(find_element_by_id(driver, "com.jd.jdlite:id/navigation_fragment")):
        driver.back()
        s_sleep()

