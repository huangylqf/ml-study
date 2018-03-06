from selenium import webdriver
import os
import time

chromedriver = "C:/tool/Python36/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

url = "http://182.131.21.139/gspt/ccm-action/domesticgame/searchGame"
browser.get(url)

for x in range(1, 2216):
    doc_list = browser.find_element_by_class_name("content-top").find_elements_by_tag_name("li")

    xh, bawh, yymc, pwrq = "", "", "", ""
    for doc in doc_list:
        id = doc.get_attribute("id")
        if id == 'xh':
            xh, bawh, yymc, pwrq = "", "", "", ""
            xh = doc.text
        elif id == 'bawh':
            bawh = doc.text
        elif id == 'yymc':
            yymc = doc.text
        elif id == 'pwrq':
            pwrq = doc.text

        if "0956" in bawh:
            print(x, xh, bawh, yymc, pwrq)
            browser.quit()

    # 自动翻到下一页
    time.sleep(1)
    next = browser.find_element_by_class_name("content-fy").find_element_by_link_text("下一页")
    next.click()

# 关闭浏览器
# browser.quit()
