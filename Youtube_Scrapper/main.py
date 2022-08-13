from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time
import os
import wget
driver_path = 'D:/Programming/Drivers/chromedriver.exe'
c_path = os.getcwd()
w_path = os.path.join(c_path, 'images')
l_path = os.path.join(c_path,'Links')
links = open(f'{l_path}\Links.txt', 'r')
links_reader = links.readlines()
links.close()
all_links = [link[:-1] for link in links_reader]
print('\nLENGTH OF ALL_LINKS:=>' ,len(all_links))
src = []

src_modify = []

links_file = open(f'{l_path}\Links.txt', 'a')

url = "https://www.youtube.com"



try:
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_argument('headless')
    chrome_options.add_experimental_option("prefs",prefs)
except:
    print('Somthing went wrong!')
else:
    driver = webdriver.Chrome(executable_path = driver_path ,chrome_options=chrome_options)
    driver.get(url)
    # time.sleep(10)

    print(w_path)
    print(l_path)


    i = 0
    height = 0
    while True:
        if i%50 == 0:
            print('\nREFRESING PAGE.......')
            driver.get(url)
        print('\nAFTER CLEAR LENGTH OF SRC_MODIFY:=> ', len(src_modify))
        print('\nAFTER CLEAR LENGTH OF SRC:=> ', len(src))
        i+=1
        time.sleep(5)
        print('\nROUND:=> ',i)
        driver.execute_script(f"window.scrollTo(0,{height});")
        try:
            images = driver.find_elements_by_tag_name('img')
            # print('IMG: ', img)
            src = [image.get_attribute('src') for image in images]
        except:
            height+=1500
            pass
        else:
            height+=1500
            src_modify = [i for i in src if i]
            # print('SRC: ',src_modify)
            print('\nLENGTH OF SRC_MODIFY:=> ', len(src_modify))
            print('\nLENGTH OF SRC:=> ', len(src))
            j= 0 
            for l in src_modify:
                if not 'yt3.ggpht.com' in l and l not in all_links:
                    # print('L: ', l)
                    links_file.write(f'{l}\n')
                    all_links.append(l)
                    j = int(j)
                    j+=1
                    save_as = os.path.join(w_path,'image'+str(i)+str(j)+'.png')
                    try:
                        wget.download(l,save_as)
                    except:
                        pass
            print('\nLENGTH OF ALL_LINKS:=> ', len(all_links))
            src.clear()
            src_modify.clear()


links_file.close()