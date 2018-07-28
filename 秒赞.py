from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os 
import sys
#----------------------_init_----------------------------------------------------------
py_list = sys.path[0]                       #当前运行目录
endTime = int(time.strftime("%I")) + 2      #何时结束程序 重新获得cookie
count = 0                   #一轮点了多少个
assist_num = 0              #辅助判断是否加载其他说说
all_num = 0                 #本次运行一共点了多少赞
page_down_times = 0         #向下翻页翻了几次
username = 'xxxxxx'     #QQ账号
password = 'xxxxxx'     #QQ密码
times = 0                   #第几轮点赞
if endTime > 12 :           #转换时间
   endTime = endTime - 12 
   pass

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
#driver = webdriver.Chrome()
driver.get('https://i.qq.com/')

def login ():
    time.sleep(1)
    driver.maximize_window()
    driver.switch_to_frame('login_frame')
    driver.find_element_by_id('switcher_plogin').click()  
    driver.find_element_by_id('u').send_keys(username) 
    driver.find_element_by_id('p').send_keys(password)
    driver.find_element_by_id('login_button').click()
    time.sleep(2)
    driver.find_element_by_id('goto_top_btn') #回到顶部解决第一条点不到的问题
    driver.execute_script('window.scrollTo(0,100);')

def give_like ():
    global count
    global assist_num 
    global page_down_times 
    global endTime
    global all_num
    global times
    while True :
#-------------------------------------向下加载说说--------------------------------------------------------------        
        if  assist_num == count and times != 0 :                         #如果本轮没有点赞则将页面拉到最下 使QQ空间加载说说
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight);') 
            page_down_times += 1 
        assist_num = count
 #--------------------------------------点赞逻辑----------------------------------------------------------------       
        data = driver.find_elements_by_css_selector('.item.qz_like_btn_v3 ')
        for i in data :
            try:
                if i.get_attribute('data-clicklog') == 'like' :
                    try:
                        i.click()
                        count += 1
                        all_num += count
                    except:
                        try:
                            driver.execute_script('window.scrollTo(0,150);')
                            i.click()
                            count += 1
                            all_num += count
                        except:
                            continue
            except:
                continue
        
        times += 1
        print('本次运行已累计点赞{}条说说'.format(all_num))
        #print(page_down_times,count,assist_num)
#---------------------------------点完一轮赞，休息一会-----------------------------------------------------------        
        if (count) >= 100 or (page_down_times >= 10) :            #如果单个循环运行点赞次数超过100个或者向下5页都已经全部被赞 则刷新页面 脚本初始化  并且休息10min
            print('休息10min')
            time.sleep(5)
            page_down_times = 0                                   #当然如果你的好友10分钟能刷出100条说说  我真是孤陋寡闻了。
            count = 0                                             #如果你想实现秒赞 将600改成1  当然就要牺牲一些cpu
            assist_num = 0
            driver.refresh()
            #driver.find_element_by_xpath('//*[@id="tab_menu_friend"]/div[3]').click()#防止被好友点赞跳转到 "与我相关"
            driver.find_element_by_id('goto_top_btn')              #回到顶部
            driver.execute_script('window.scrollTo(0,100);')       #下拉一部分至第一条说说处 
#---------------------------------------重启以防止cookies过气-----------------------------------------------------
        if int(time.strftime("%I")) == endTime :                   #每两个小时重新登陆一次
            driver.close()
            os.startfile(py_list+ '\秒赞.py')
            driver.quit()
            os._exit()
            
login()
give_like()
        
