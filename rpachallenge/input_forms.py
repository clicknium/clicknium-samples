from clicknium import clicknium as cc, locator
import requests,os
import pandas as pd

tab = cc.chrome.open("https://rpachallenge.com/")
tab.find_element(locator.chrome.rpachallenge.a_inputforms).click()
href = tab.find_element(locator.chrome.rpachallenge.a_downloadexcelcloud_download).get_property("href")
url = os.path.join("https://rpachallenge.com/", href)
excelFile = requests.get(url)
temp_file = os.path.join(os.getcwd(), 'challenge.xlsx')
open(temp_file, 'wb').write(excelFile.content)
data = pd.read_excel(temp_file)

tab.find_element(locator.chrome.rpachallenge.button_start).click()
for idx, item in data.iterrows():
    tab.find_element(locator.chrome.rpachallenge.text_input, {'label':'First Name'}).set_text(item[0])
    tab.find_element(locator.chrome.rpachallenge.text_input, {'label':'Last Name'}).set_text(item[1])
    tab.find_element(locator.chrome.rpachallenge.text_input, {'label':'Company Name'}).set_text(item[2])
    tab.find_element(locator.chrome.rpachallenge.text_input, {'label':'Role in Company'}).set_text(item[3])
    tab.find_element(locator.chrome.rpachallenge.text_input, {'label':'Address'}).set_text(item[4])
    tab.find_element(locator.chrome.rpachallenge.text_input, {'label':'Email'}).set_text(item[5])
    tab.find_element(locator.chrome.rpachallenge.text_input, {'label':'Phone Number'}).set_text(str(item[6]))
    tab.find_element(locator.chrome.rpachallenge.submit_submit).click()

print('done')