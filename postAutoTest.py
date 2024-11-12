import unittest
from appium import webdriver
from appium.webdriver.common.by import By
from appium.webdriver.support.ui import WebDriverWait
from appium.webdriver.support import expected_conditions as EC


class NewsSiteTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()



    def test_article_comment(self):
        driver = self.driver
        #  假设一个网易新闻内容详情页地址
        driver.get("https://c.m.163.com/news/a")

        # 找到发帖框并输入内容
        comment_box = driver.find_element(By.ID, "comment_box")
        comment_box.send_keys("This is a test comment.")

        # 找到提交按钮并点击
        submit_button = driver.find_element(By.ID, "submit_comment")
        submit_button.click()

        # 等待评论提交成功提示
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "comment_success"))
        )

        # 验证评论是否出现在页面上
        self.assertIn("This is a test comment.", driver.page_source)

    def tearDown(self):
        self.driver.close()


