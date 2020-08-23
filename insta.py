from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import datetime
date = datetime.datetime.now()
date = int(date.strftime("%H"))
if date >= 12 and date <=18 :
      na = "Good Afternoon "
elif date <= 12:
      na = "Good Morning "
elif date >= 19 and date < 24 :
      na = "Good Evening "
browser = webdriver.Firefox(executable_path="C:\\Users\\madhan\\Documents\\py automation\\geckodriver-v0.26.0-win64\\geckodriver.exe")
browser.get("https://www.instagram.com/")
time.sleep(5)
browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys("jus_to_explore")
browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys("madhan@20")
browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div").click()
time.sleep(10)
browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
time.sleep(5)
browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
time.sleep(2)
browser.find_element_by_css_selector(".xWeGp").click()
time.sleep(5)
i = 0 
res = True
l = ["hi" , "hey" , "hello" , "oi" ]
dos = ["whatareyoudoing","whatrudoing","whatru2ing"]
eat = ["saptiya","saptacha","ate"]
quit = ["bye","hmm","busy"]


while(res):
      try:
            browser.find_element_by_css_selector("._41V_T").click()
            time.sleep(5)
            # work here after create boting
            a = browser.find_element_by_class_name("R19PB").text.lower()
            a = a.replace(" ","")
            for i,j,k,q in zip(l,dos,eat,quit):
                  if i in a:
                        time.sleep(1)
                        browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("Hiii "+na+"!")
                        browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
                        break
                  elif j in a:
                        time.sleep(1)
                        browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("Going along with a time..what about you..?")
                        browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
                        break
                  elif k in a:
                        time.sleep(1)
                        browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("yep..you..?")
                        browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
                        break
                  elif q in a:
                        if date >= 18 and date < 24:
                              time.sleep(1)
                              browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("Hmm..bubye"+"\n"+"Time to sleep good night have a sweet dreams...")
                              browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
                              break
                        else:
                              time.sleep(1)
                              browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("Hmm..bubye")
                              browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
                              break

            else:
                  time.sleep(1)
                  browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("Hmm...then..?")
                  browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
            browser.execute_script("window.history.go(-1)")
            
      except NoSuchElementException:
            res = False
            time.sleep(5)
            print("checking....")
            res = True

      time.sleep(5)
      res = True
browser.quit()
"""time.sleep(2)
            browser.get("https://www.instagram.com/")
            while(res):
                  j = "window.scrollTo("+str(i)+","+str(i+200)+")"
                  i+=200
                  browser.execute_script(j)
                  time.sleep(2)
                  if i>10000:
                        break"""