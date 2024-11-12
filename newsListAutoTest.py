import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

# 配置项
desired_caps = {
    "platformName": "Android",
    "deviceName": "your_device_name",
    "appPackage": "com.ss.android.article.news",
    "appActivity": "com.ss.android.article.news.activity.MainActivity"
}

# 启动Appium驱动
driver = webdriver.Remote("http://localhost:8080/wd/hub", desired_caps)

# 等待主页加载
time.sleep(5)

# 检查是否成功进入主页
try:
    headline_title = driver.find_element_by_id("headline_title_id")
    assert headline_title.is_displayed()
    print("成功进入主页，头条标题显示正常")
except Exception as e:
    print("进入主页失败或头条标题未正常显示:", e)

# 模拟向下滑动
screen_size = driver.get_window_size()
start_x = screen_size['width'] / 2
start_y = screen_size['height'] * 0.8
end_y = screen_size['height'] * 0.2
driver.swipe(start_x, start_y, start_x, end_y, 500)
print("已执行向下滑动操作")

# 点击一个头条
try:
    headline = driver.find_element_by_id("headline_id")
    headline.click()
    print("成功点击头条新闻，进入新闻详情页")
except Exception as e:
    print("点击头条失败:", e)

# 在新闻详情页，模拟返回操作
try:
    back_button = driver.find_element_by_id("back_button_id")
    back_button.click()
    print("成功从新闻详情页返回主页")
except Exception as e:
    print("返回主页失败:", e)

# 关闭驱动
driver.quit()