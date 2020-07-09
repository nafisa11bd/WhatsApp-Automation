from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome('chromedriver.exe',options=chrome_options)
#Here I have specified the location of my chromedriver

driver.get("https://web.whatsapp.com")
#link for redirecting whatsapp
#you have to scan qr before inputting values
number,msg,filepath=input().split('~')
#taking 3 inputs the number of whom you will send message to, the text you want to send and the directory of an image attachment you want to send those 3 values should be separated by ~
if number.isnumeric()==True:
    number = '+88' + number
    number = number[:4] + ' ' + number[4:]
    number = number[:9] + '-' + number[9:]



#separating numberby space and hyfen to get the format +880 xxxx-xxxxxx



user=driver.find_element_by_xpath('//span[@title="{}"]'.format(number))
user.click()
#finding number and click it
message_box=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
message_box.send_keys(msg)
#putting message
driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")
sleep(3)
attachment_icon=driver.find_element_by_xpath('//div[@title="Attach"]')
attachment_icon.click()
#clicking attachment icon
image_icon=driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_icon.send_keys(filepath)
#attaching file to send
sleep(4)
#sleep as there is little delay of opening the button
send_button=driver.find_element_by_xpath('//span[@data-icon="send"]')
send_button.click()
#clicking send button







