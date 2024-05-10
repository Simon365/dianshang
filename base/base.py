# coding=utf-8
import time
from appium import webdriver
import os
import re
import xml.etree.cElementTree as et
from random import *
from functools import wraps
# from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.common import exceptions
from typing import Dict, List, Optional, TypeVar, Union

T = TypeVar('T', bound='WebElement')


def sleep(t):
    time.sleep(t)


def pause():
    time.sleep(1)


def s_sleep():
    time.sleep(5)


def m_sleep():
    time.sleep(10)


def l_sleep():
    time.sleep(15)


def rand_sleep_after(func):
    @wraps(func)
    def _deco(*args, **kwargs):
        func(*args, **kwargs)
        time.sleep(randint(1, 5))

    return _deco


@rand_sleep_after
def swipedown(driver, t=300, n=1):
    # get screen size
    try:
        size = driver.get_window_size()
        w = size['width']  # get the screen width
        h = size['height']  # get the screen height
        pause()
        x1 = w / 2
        y1 = 4 * h / 5
        y2 = h / 2
        for i in range(n):
            driver.swipe(x1, y1, x1, y2, t)
    except exceptions.WebDriverException as e:
        print(format(e))
        return


@rand_sleep_after
def swipeup(driver, t=400, n=1):
    # get screen size
    size = driver.get_window_size()
    w = size['width']  # get the screen width
    h = size['height']  # get the screen height
    s_sleep()
    x1 = w / 2
    y2 = 3 * h / 4
    y1 = h / 4
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


def swipeleft(driver, t=500, n=1):
    # get screen size
    size = driver.get_window_size()
    w = size['width']  # get the screen width
    h = size['height']  # get the screen height
    s_sleep()
    y1 = h / 2
    x1 = 3 * w / 4
    x2 = w / 4
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)


def swiperight(driver, t=500, n=1):
    # get screen size
    size = driver.get_window_size()
    w = size['width']  # get the screen width
    h = size['height']  # get the screen height
    s_sleep()
    y1 = h / 2
    x2 = 3 * w / 4
    x1 = w / 4
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)


def exist(element):
    flag = True
    try:
        element.location
    except Exception as e:
        print(format(e))
        flag = False

    return flag


def snap(driver, filename):
    # get the screen snap
    driver.get_screenshot_as_file(filename)


# snap and record the test result
def snap_record_succ(driver, image_path, ws_test, line_no, desc) -> int:
    image = image_path + str(line_no).zfill(4) + desc + ".png"
    snap(driver, image)
    ws_test.write(line_no, 0, desc)  # 记录测试用例名称
    ws_test.write(line_no, 1, "通过")  # 记录测试用例结果
    ws_test.write(line_no, 2, "\mp\\" + desc)  # 记录测试用例结果
    pause()
    return line_no + 1


# snap and record the test result while test failed
def snap_record_fail(driver, image_path, ws_test, line_no, desc) -> int:
    image = image_path + str(line_no).zfill(4) + desc + ".png"
    snap(driver, image)
    ws_test.write(line_no, 0, desc)  # 记录测试用例名称
    ws_test.write(line_no, 1, "失败")  # 记录测试用例结果
    ws_test.write(line_no, 2, "\mp\\" + desc)  # 记录测试用例结果
    pause()
    return line_no + 1


# find the element by id and title
def find_element_by_id_title(driver, rid, title) -> webdriver.WebElement:
    obj = driver.find_elements(By.ID, rid)
    for i in range(len(obj)):
        if obj[i].text == title:
            return obj[i]


# find the element by class and title
def find_element_by_class_title(driver, classname, title) -> webdriver.WebElement:
    obj = driver.find_elements_by_class_name(classname)
    for i in range(len(obj)):
        if obj[i].text == title:
            return obj[i]


def find_element_by_name(driver, name) -> webdriver.WebElement:
    try:
        obj = driver.find_element_by_android_uiautomator('new UiSelector().text("' + name + '")')
        return obj
    except Exception as e:
        print(format(e))
        print(" Find the element " + name + " failed!")


def find_element_by_content_desc(driver, desc):
    try:
        obj = driver.find_element_by_accessibility_id(desc)
        return obj
    except Exception as e:
        print(format(e))
        print(" Find the element " + desc + " failed!")


def find_element_by_index(driver, index) -> webdriver.WebElement:
    try:
        obj = driver.find_element_by_android_uiautomator('new UiSelector().index(' + index + ')')
        return obj
    except Exception as e:
        print(format(e))
        print(" Find the element by index failed!")


def find_element_by_id(driver, id) -> webdriver.WebElement:
    try:
        # obj = driver.find_element_by_id(id)
        obj = driver.find_element(By.ID, id)
        return obj
    except Exception as e:
        print(format(e))
        print(" Find the element by id failed!")


def find_element_by_ID_index_clickable(driver, id, index) -> webdriver.WebElement:
    try:
        obj = driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId(' + id + ').index(' + index + ').clickable(true)')
        return obj
    except Exception as e:
        print(format(e))
        print(" Find the element by " + id + " failed!")


def find_elements_by_ID(driver, id) -> List[T]:
    return driver.find_elements(By.ID, id)


# launch the specific app
def launch_app(driver, appname):
    try:
        find_element_by_name(driver, appname).click()
        m_sleep()
        return True
    except Exception as e:
        print("launch the app " + appname + " failed!")
        return False


# initialize the device
def peer_SetUp(self, deviceid, version):
    # Android environment
    desired_caps = {
        'platformName': 'android',  # platform name
        'deviceName': deviceid,  # device name
        'platformVersion': version,  # platform version
        'noReset': True,  # reinstall the app or not
        'recreateChromeDriverSessions': True,  #
        'unicodeKeyboard': False,  # True, disable the device input method
        'resetKeyboard': False,  # True, enable the appium keyboard
        'chromedriverExecutable': 'D:/chromedriver/chromedriver.exe',
        'ensureWebviewsHavePages': True,  # appium augment its webview detection or not
        'skipLogcatCapture': False,  # skip logcat
        # 'appPackage':'com.tencent.mm',          # package name
        # 'appActivity':'.ui.LauncherUI',         # launch page
        # 'chromeOptions':{"androidProcess": "com.tencent.mm:appbrand0"},
        # 'chromedriverExecutableDir':'E:/tool/appium'  # auto research the compatible chromedriver directory
    }

    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    # self.driver = webdriver.webdriver.WebDriver(command_executor='http://localhost:4723/wd/hub',
    #                                             desired_capabilities=desired_caps)
    m_sleep()


# initialize the device
def peer_setup4(self, deviceid, version):
    # Android environment
    kwarg = {
        'platformName': 'android',  # platform name
        'deviceName': deviceid,  # device name
        'platformVersion': version,  # platform version
        'noReset': 'True',  # reinstall the app or not
        'recreateChromeDriverSessions': 'True',  #
        'unicodeKeyboard': 'false',  # True, disable the device input method
        'resetKeyboard': 'false',  # True, enable the appium keyboard
        'chromedriverExecutable': 'E:/tool/appium/chromedriver.exe',
        'ensureWebviewsHavePages': 'True',  # appium augment its webview detection or not
        'skipLogcatCapture': 'false'  # skip logcat
        # 'appPackage':'com.tencent.mm',          # package name
        # 'appActivity':'.ui.LauncherUI',         # launch page
        # 'chromeOptions':{"androidProcess": "com.tencent.mm:appbrand0"},
        # 'chromedriverExecutableDir':'E:/tool/appium'  # auto research the compatible chromedriver directory
    }

    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', kwarg)
    # self.driver = webdriver.webdriver.WebDriver(command_executor='http://localhost:4723/wd/hub',
    #                                             desired_capabilities=desired_caps)
    m_sleep()


# login the micromsg
def login_micromsg(driver, username, pword):
    try:
        psw = driver.find_element_by_class_name("android.widget.EditText")
        pause()
        psw.click()
        pause()
        psw.send_keys(pword)
        pause()
        login = driver.find_elements_by_class_name("android.widget.Button")
        pause()
        login[1].click()
    except Exception as e:
        print(format(e))
        l_sleep()


# enter micromsg assistant
def enterMicromsgAssistant(driver, mp):
    # open mp panel
    swipedown(driver)
    l_sleep()

    # open the specific mp
    try:
        driver.find_element_by_accessibility_id(mp).click()
        l_sleep()
    except Exception as e:
        print(format(e))
        print('打开指定小程序失败！')


# launch specific app
def launch_specific_app(driver, appname):
    try:
        driver.find_element_by_accessibility_id(appname).click()
        l_sleep()
        return True
    except Exception as e:
        print(format(e))
        print("打开程序 " + appname + " 失败！")
        return False


# find the element on the webview in the app
def el_in_view(deviceid, attri, text) -> bool:
    flag = False
    m_sleep()
    os.popen('adb -s' + ' ' + deviceid + ' ' + 'shell uiautomator dump --compressed /data/local/tmp/uidump.xml')
    m_sleep()
    os.popen('adb -s' + ' ' + deviceid + ' ' + 'pull data/local/tmp/uidump.xml D:\\workspace\\boxmp\\uidump.xml')
    m_sleep()
    source = et.parse("uidump.xml")
    root = source.getroot()

    for node in root.iter("node"):
        if node.attrib[attri] == text:
            pause()
            flag = True
            pause()
            break
    return flag


# find the element on the webview in the app and tap it
def click_el_in_view(driver, deviceid, attri, text) -> bool:
    flag = False
    m_sleep()
    os.popen('adb -s' + ' ' + deviceid + ' ' + 'shell uiautomator dump --compressed /data/local/tmp/uidump.xml')
    m_sleep()
    os.popen('adb -s' + ' ' + deviceid + ' ' + 'pull data/local/tmp/uidump.xml D:\\workspace\\boxmp\\uidump.xml')
    m_sleep()
    source = et.parse("uidump.xml")
    root = source.getroot()

    for node in root.iter("node"):
        if node.attrib[attri] == text:
            bounds = node.attrib["bounds"]
            pattern = re.compile(r"\d+")
            coord = pattern.findall(bounds)
            x = (int(coord[0]) + int(coord[2])) / 2
            y = (int(coord[1]) + int(coord[3])) / 2
            driver.tap([[x, y]])
            l_sleep()
            flag = True
            pause()
            break
    return flag
