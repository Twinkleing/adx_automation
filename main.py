import os
import random

from pywinauto import application
from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

WEBSITE_URL = "http://adx.com/hl/app"
GOOGLE_PLAY_URL = "https://play.google.com/store/apps/collection/cluster?clp=ogowCAESBkZBTUlMWRocChZyZWNzX3RvcGljXzY0V2pXNW5scXBFEDsYAyoCCANSAggC:S:ANO1ljLYtu8&gsr=CjOiCjAIARIGRkFNSUxZGhwKFnJlY3NfdG9waWNfNjRXalc1bmxxcEUQOxgDKgIIA1ICCAI%3D:S:ANO1ljL4ijo"
TIME_ONE = 1
TXT = "Selenium automated creation: "
USERNAME_XPATH = "//*[@id=\"loginCard\"]/div[2]/form/div[1]/div/div/input"
USER_NAME = "adx_test4"
PASSWORD_XPATH = "//*[@id=\"loginCard\"]/div[2]/form/div[2]/div/div/input"
USER_PWD = "abc123@abc123.Com"
LOGIN_CARD = "//*[@id=\"loginCard\"]/div[2]/form/div[3]/div/button"
LOGIN = "el-button--primary"
MY_APP = "//*[@id=\"layout\"]/aside/div/ul/li[1]"
ADD_APP = "add-app-btn"
ADD_AD = "//*[@id=\"layout\"]/section/main/div/div/div[1]/div[3]/div[3]/table/tbody/tr[1]/td[6]/div/span[2]"
AD_TYPE = "//*[@id=\"layout\"]/section/main/div/div/div[position()>=1]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[1]/form/div[1]/div[2]/div/div/div/div"
BANNER_AD = "/html/body/div[position()>=1]/div/div/div/div[2]/div[1]/div/div/div[1]"
VAST_AD = "/html/body/div[position()>=1]/div/div/div/div[2]/div[1]/div/div/div[2]"
INSERT_AD = "/html/body/div[position()>=1]/div/div/div/div[2]/div[1]/div/div/div[3]"
REWARD_AD = "/html/body/div[position()>=1]/div/div/div/div[2]/div[1]/div/div/div[4]"
BANNER_SIZE = "adSize"
AD_NAME = "adName"
ZK = "//*[@id=\"layout\"]/section/main/div/div/div/div[3]/div[3]/table/tbody/tr[1]/td[5]/div"
AD_ID = "//*[@id=\"layout\"]/section/main/div/div/div/div[3]/div[3]/table/tbody/tr[2]/td/div/div/div/div[3]/table/tbody/tr/td[2]/div"
AD_FORMAT = "//*[@id=\"layout\"]/section/main/div/div/div/div[3]/div[3]/table/tbody/tr[2]/td/div/div/div/div[3]/table/tbody/tr/td[4]/div"
HL_CONTROLLER = "//*[@id=\"layout\"]/aside/div/ul/li[2]"
CREAT_HL_ACTIVITY = "create_primary"
PROMOTE_APP = "ant-select-selection-search-input"
PROMOTE_SEL = "/html/body/div[position()>=1]/div/div/div/div[2]/div[1]/div/div/div[2]/div"
HL_NAME = "hlpromotion"
SEL_AD = "select"
SEL_AD_SEL = "//*[@id=\"layout\"]/section/main/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/ul/li/span[1]"
SEL_AD_OK = "//*[@id=\"layout\"]/section/main/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/ul/li/ul/li/span[2]/span"
SEL_AD_SAVE = "//*[@id=\"layout\"]/section/main/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[4]/button"
HL_CONTINUE = "//*[@id=\"layout\"]/section/main/div/div[1]/div[3]/div[1]/div[2]/div[9]/button[1]"
ADD_CREATIVE = "//*[@id=\"layout\"]/section/main/div/div[1]/div[3]/div[2]/div[2]/div[1]/div"
BANNER_CREATIVE = "/html/body/div[6]/div/div/div/div[2]/div[1]/div/div/div[1]/div"
VAST_CREATIVE = "/html/body/div[6]/div/div/div/div[2]/div[1]/div/div/div[2]/div"
INSERT_CREATIVE = "/html/body/div[6]/div/div/div/div[2]/div[1]/div/div/div[3]/div"
VIDEO_CREATIVE = "/html/body/div[6]/div/div/div/div[2]/div[1]/div/div/div[4]/div"
CREATIVE_NAME = "creativeName"
CREATIVE_TITLE = "creativeTitle"
CREATIVE_SLOGAN = "advertisingSlogan"
CREATIVE_SEL = "selection"
CREATIVE_SIZE = "creativeSize"
CREATIVE_TEMP = "creativeTemplate"
TEMP_SEL = "/html/body/div[position()>=1]/div/div/div/div[2]/div[1]/div/div/div[1]"
UPLOAD = "//*[@id=\"layout\"]/section/main/div/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/a"
UPLOAD_IMG = "//*[@id=\"layout\"]/section/main/div/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div/div[3]/div/div/ul/li[1]/span/span/div[1]/span/span"
UPLOAD_VIDEO = "//*[@id=\"layout\"]/section/main/div/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div/div[3]/div/div/ul/li[2]/span/span/div[1]/span/span"
CREATIVE_OK = "//*[@id=\"layout\"]/section/main/div/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/table/tbody/tr/td[6]/div/span"
CREATIVE_SAVE = "saves"
COMPLETE = "//*[@id=\"layout\"]/section/main/div/div[1]/div[3]/div[2]/div[2]/div[4]/button"
CLOSE = "//*[@id=\"layout\"]/section/main/div/div/div[2]/div/div[2]/div/div[2]/button"
isMultiple = 0


def print_hi():
    print("1、多广告位创建,0、非多广告位创建")
    num = input()
    isMultiple = int(num)
    if isMultiple == 0:
        google_driver = webdriver.Chrome()
        google_driver.get(GOOGLE_PLAY_URL)
        google_driver.implicitly_wait(10)
        apps = []
        for i in range(1, 51, 1):
            url = google_driver.find_element_by_xpath(
                "//*[@id=\"fcxH9b\"]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[" + str(
                    i) + "]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
                "href")
            apps.append(url)
        google_driver.quit()
    videos = []
    for root, dirs, files in os.walk("E:\\video"):
        videos = files
        print(videos)  # 当前路径下所有非目录子文件
    mobile_driver = webdriver.Chrome()
    mobile_driver.get(WEBSITE_URL)
    mobile_driver.implicitly_wait(10)
    # 输入账号
    mobile_driver.find_element_by_xpath(USERNAME_XPATH).send_keys(USER_NAME)
    # 输入密码
    mobile_driver.find_element_by_xpath(PASSWORD_XPATH).send_keys(USER_PWD)
    # 获取验证码
    mobile_driver.find_element_by_xpath(LOGIN_CARD).click()
    time.sleep(10)
    # 点击登录
    mobile_driver.find_element_by_class_name(LOGIN).click()
    count = 0
    if isMultiple == 0:
        for app in apps:
            count = count + 1
            mobile_driver.find_element_by_xpath(MY_APP).click()
            # 添加应用
            mobile_driver.find_element_by_class_name(ADD_APP).click()
            # 输入APP链接
            mobile_driver.find_element_by_class_name("url").send_keys(app)
            # 点击保存
            mobile_driver.find_element_by_class_name("saves").click()
            time.sleep(10)
            createdAd(mobile_driver, count, videos, isMultiple)
    elif isMultiple == 1:
        for i in range(1, 100, 1):
            count = count + 1
            mobile_driver.find_element_by_xpath(MY_APP).click()
            createdAd(mobile_driver, count, videos, isMultiple)
    time.sleep(600)


def createdAd(mobile_driver, count, videos, isMultiple):
    print(str(isMultiple) + "FFFFFFFFFFF")
    # 添加广告单元
    try:
        mobile_driver.find_element_by_xpath(ADD_AD).click()
    except Exception:
        print("app已重复......")
        mobile_driver.find_element_by_xpath(CLOSE).click()
        return
        # 选择广告类型
    time.sleep(3)
    time.sleep(1)
    mobile_driver.find_element_by_xpath(AD_TYPE).click()
    ad_type = random.choice(range(4))
    time.sleep(3)

    if ad_type == 0:
        mobile_driver.find_element_by_xpath(BANNER_AD).click()
        time.sleep(3)

        mobile_driver.find_element_by_id(BANNER_SIZE).click()
        time.sleep(1)
        time.sleep(3)

        # 300*600
        mobile_driver.find_element_by_xpath(
            "/html/body/div[position()>=1]/div/div/div/div[2]/div[1]/div/div/div[8]/div").click()
    elif ad_type == 1:
        mobile_driver.find_element_by_xpath(VAST_AD).click()
    elif ad_type == 2:
        mobile_driver.find_element_by_xpath(INSERT_AD).click()
    else:
        mobile_driver.find_element_by_xpath(REWARD_AD).click()
    # 输入广告单元名称
    mobile_driver.find_element_by_id(AD_NAME).send_keys(TXT + str(count))
    # 点击保存
    time.sleep(3)

    mobile_driver.find_element_by_class_name("saves").click()
    # 展开
    time.sleep(3)

    mobile_driver.find_element_by_xpath(ZK).click()
    time.sleep(3)
    if isMultiple == 1:
        path1 = "//*[@id=\"layout\"]/section/main/div/div/div/div[3]/div[3]/table/tbody/tr[2]/td/div/div/div/div[3]/table/tbody/tr[" + str(
            count) + "]/td[2]/div"
        adId = mobile_driver.find_element_by_xpath(
            path1).text
        path2 = "//*[@id=\"layout\"]/section/main/div/div/div/div[3]/div[3]/table/tbody/tr[2]/td/div/div/div/div[3]/table/tbody/tr[" + str(
            count) + "]/td[4]/div"
        adFormat = mobile_driver.find_element_by_xpath(
            path2).text
        print(path1 + "FFFFF")
        print(path2 + "FFFFFFFF")
    else:
        adId = mobile_driver.find_element_by_xpath(AD_ID).text
        adFormat = mobile_driver.find_element_by_xpath(AD_FORMAT).text
    print(str(count) + "、广告ID：" + adId + "  广告类型：" + adFormat)
    # 换量操作中心
    mobile_driver.find_element_by_xpath(HL_CONTROLLER).click()
    time.sleep(2)
    # 点击新建换量活动
    time.sleep(3)

    mobile_driver.find_element_by_class_name(CREAT_HL_ACTIVITY).click()
    time.sleep(2)
    # 选择推广应用
    time.sleep(3)

    mobile_driver.find_element_by_class_name(PROMOTE_APP).click()
    time.sleep(3)

    mobile_driver.find_element_by_xpath(PROMOTE_SEL).click()
    # 输入换量名称
    mobile_driver.find_element_by_class_name(HL_NAME).send_keys(TXT + str(count))
    # 选择广告单元
    time.sleep(3)

    mobile_driver.find_element_by_class_name(SEL_AD).click()
    time.sleep(3)

    mobile_driver.find_element_by_xpath(SEL_AD_SEL).click()
    time.sleep(3)

    if isMultiple == 1:
        path = "//*[@id=\"layout\"]/section/main/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/ul/li[1]/ul/li[" + str(
            count) + "]/span[2]/span"
        print(path + "FFFFFFF")
        mobile_driver.find_element_by_xpath(
            path).click()
    else:
        mobile_driver.find_element_by_xpath(SEL_AD_OK).click()
    time.sleep(3)

    # 点击保存
    mobile_driver.find_element_by_xpath(SEL_AD_SAVE).click()
    # 保存继续
    mobile_driver.find_element_by_xpath(HL_CONTINUE).click()
    time.sleep(2)
    # 添加创意
    mobile_driver.find_element_by_xpath(ADD_CREATIVE).click()
    time.sleep(1)
    if ad_type == 0:
        mobile_driver.find_element_by_xpath(BANNER_CREATIVE).click()
        mobile_driver.find_element_by_id(CREATIVE_NAME).send_keys(TXT + str(count))
        mobile_driver.find_element_by_id(CREATIVE_SIZE).click()
        time.sleep(1)
        mobile_driver.find_element_by_xpath(
            "/html/body/div[7]/div/div/div/div[2]/div[1]/div/div/div[8]/div").click()
    elif ad_type == 1:
        mobile_driver.find_element_by_xpath(VAST_CREATIVE).click()
        mobile_driver.find_element_by_id(CREATIVE_NAME).send_keys(TXT + str(count))
        mobile_driver.find_element_by_id(CREATIVE_TITLE).send_keys(TXT + str(count))
        mobile_driver.find_element_by_id(CREATIVE_SLOGAN).send_keys(TXT + str(count))
    elif ad_type == 2:
        mobile_driver.find_element_by_xpath(INSERT_CREATIVE).click()
        mobile_driver.find_element_by_id(CREATIVE_NAME).send_keys(TXT + str(count))
    else:
        mobile_driver.find_element_by_xpath(VIDEO_CREATIVE).click()
        mobile_driver.find_element_by_id(CREATIVE_NAME).send_keys(TXT + str(count))
        mobile_driver.find_element_by_id(CREATIVE_TITLE).send_keys(TXT + str(count))
        mobile_driver.find_element_by_id(CREATIVE_SLOGAN).send_keys(TXT + str(count))
    mobile_driver.find_element_by_id(CREATIVE_TEMP).click()
    time.sleep(1)
    mobile_driver.find_element_by_id(CREATIVE_TEMP).send_keys(Keys.ENTER)
    time.sleep(1)
    mobile_driver.find_element_by_class_name(CREATIVE_SEL).click()
    time.sleep(1)
    mobile_driver.find_element_by_xpath(UPLOAD).click()
    if ad_type == 1:
        mobile_driver.find_element_by_xpath(UPLOAD_VIDEO).click()
    else:
        mobile_driver.find_element_by_xpath(UPLOAD_IMG).click()
    time.sleep(1)
    app = application.Application()  # 实例化Application
    app.connect(found_index=0, class_name='#32770')  # 根据class_name找到弹出窗口
    randomNum = random.choice(range(10))
    if ad_type == 1:
        filepath = "E:\\video\\" + videos[randomNum]
    else:
        filepath = "C:\\Users\kuangbaoting\Pictures\dsa.png"
    app["Dialog"]["Edit1"].type_keys(filepath)  # 在输入框中输入值
    app["Dialog"]["Button1"].click()
    time.sleep(5)
    mobile_driver.find_element_by_xpath(CREATIVE_OK).click()
    mobile_driver.find_element_by_class_name(CREATIVE_SAVE).click()
    try:
        mobile_driver.find_element_by_xpath(COMPLETE).click()
    except Exception:
        print(str(count) + " 广告创建失败")
        mobile_driver.find_element_by_xpath(HL_CONTROLLER).click()


if __name__ == '__main__':
    print_hi()
