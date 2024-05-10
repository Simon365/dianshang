from base.base import *


def qh_browse_video(driver, times):
    for i in range(0, times):
        swipedown(driver)
        print("第%s个......" % i)
        # print("正在浏览第%s个视频......" % i)


# guanggao xuanshang
def qh_ad_video(driver, times):
    i = 0
    j = 0

    for i in range(0, times):
        try:
            # el = driver.find_element_by_android_uiautomator(
            #     'new UiSelector().className("android.widget.Button").index(1).text("福利")')
            # s_sleep()
            # el.click()
            print("第%s次点击福利入口......" % i)
            driver.tap([(490, 250)])
            m_sleep()
            time.sleep(randint(25, 35))
            driver.back()
            s_sleep()

            # close = find_element_by_ID_index_clickable(driver, 'com.kuaishou.nebula:id/video_close_icon', 1)
            # while close is None:
            #     s_sleep()
            #     j = j + 1
            #     if (j > 3):
            #         driver.back()
            #         s_sleep()
            #         break
            #     close = find_element_by_ID_index_clickable(
            #         driver, 'com.kuaishou.nebula:id/video_close_icon', 1)
            # close.click()
            # s_sleep()
        except Exception as e:
            print(format(e))
            print("没有找到福利入口！")


# zhiborenwu
def qh_zhibo_video(driver, times):
    i = 1
    for i in range(1, times + 1):
        try:
            # el = driver.find_element_by_android_uiautomator(
            #     'new UiSelector().className("android.widget.Button").index(1).text("福利")')
            # s_sleep()
            # el.click()
            print("第%s次点击直播任务入口......" % i)
            objs = driver.find_elements_by_id("com.kuaishou.nebula:id/live_surface")
            s_sleep()
            objs[0].click()
            l_sleep()
            time.sleep(randint(40, 50))
            driver.back()
            s_sleep()

            # close = find_element_by_ID_index_clickable(driver, 'com.kuaishou.nebula:id/video_close_icon', 1)
            # while close is None:
            #     s_sleep()
            #     j = j + 1
            #     if (j > 3):
            #         driver.back()
            #         s_sleep()
            #         break
            #     close = find_element_by_ID_index_clickable(
            #         driver, 'com.kuaishou.nebula:id/video_close_icon', 1)
            # close.click()
            # s_sleep()
        except Exception as e:
            print(format(e))
            print("没有找到直播任务入口！")
