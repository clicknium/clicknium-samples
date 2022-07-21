from datetime import datetime
import os
import requests
from clicknium import clicknium as cc, locator
import pandas as pd

def main():
    tab = cc.edge.open("https://developer.automationanywhere.com/challenges/automationanywherelabs-customeronboarding.html")
    url = tab.find_element(locator.customeronboarding.developer.a_downloadcsv).get_property("href")
    excelFile = requests.get(url)
    temp_file = os.path.join(os.getcwd(), 'missing.csv')
    open(temp_file, 'wb').write(excelFile.content)
    data = pd.read_csv(temp_file)

    print("[clicknium] Start to fill data:{}".format(datetime.now()))
    for idx, item in data.iterrows():
        tab.find_element(locator.customeronboarding.developer.text_customername).set_text(item[0])
        tab.find_element(locator.customeronboarding.developer.text_customerid).set_text(item[1])
        tab.find_element(locator.customeronboarding.developer.text_primarycontact).set_text(item[2])
        tab.find_element(locator.customeronboarding.developer.text_street).set_text(item[3])
        tab.find_element(locator.customeronboarding.developer.text_city).set_text(item[4])
        tab.find_element(locator.customeronboarding.developer.select_state).select_item(item[5])
        tab.find_element(locator.customeronboarding.developer.text_zip).set_text("%05d" % item[6])
        tab.find_element(locator.customeronboarding.developer.email_email).set_text(item[7])
        if item[8] == "YES":
            tab.find_element(locator.customeronboarding.developer.radio_activediscountyes).set_checkbox()
        else:
            tab.find_element(locator.customeronboarding.developer.radio_activediscountno).set_checkbox()
        
        if item[9] == "YES":
            nda = 'check'
        else:
            nda = 'uncheck'
        tab.find_element(locator.customeronboarding.developer.checkbox_nda).set_checkbox(check_type=nda)
        tab.find_element(locator.customeronboarding.developer.button_submit_button).click()
    print("[clicknium] End to fill data:{}".format(datetime.now()))

if __name__ == "__main__":
    main()
