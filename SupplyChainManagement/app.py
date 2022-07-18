import os
import requests
from clicknium import clicknium as cc, locator, ui
import pandas as pd

def main():
    tab = cc.edge.open("https://developer.automationanywhere.com/challenges/automationanywherelabs-supplychainmanagement.html")
    url = tab.find_element(locator.supplychainmanagement.developer.a_downloadagentterritoryspreadsheet).get_property("href")
    excelFile = requests.get(url)
    temp_file = os.path.join(os.getcwd(), 'test.xlsx')
    open(temp_file, 'wb').write(excelFile.content)
    data = pd.read_excel(temp_file,header=1)
    
    proc_tab = cc.edge.open("https://developer.automationanywhere.com/challenges/AutomationAnywhereLabs-POTrackingLogin.html")
    proc_tab.find_element(locator.supplychainmanagement.developer.email_inputemail).set_text("admin@procurementanywhere.com")
    proc_tab.find_element(locator.supplychainmanagement.developer.password_inputpassword).set_text("paypacksh!p")
    proc_tab.find_element(locator.supplychainmanagement.developer.button_signin).click()

    po_elements = tab.find_elements(locator.supplychainmanagement.developer.text_ponumber)
    date_elements = tab.find_elements(locator.supplychainmanagement.developer.text_shipdate)
    total_elements = tab.find_elements(locator.supplychainmanagement.developer.text_ordertotal)
    agent_elements = tab.find_elements(locator.supplychainmanagement.developer.select_agent)
    count = len(po_elements)

    for i in range(count):
        po = po_elements[i].get_text()
        proc_tab.find_element(locator.supplychainmanagement.developer.search).set_text(po)
        state = proc_tab.find_element(locator.supplychainmanagement.developer.td, {"column":5}).get_text()
        ship_date = proc_tab.find_element(locator.supplychainmanagement.developer.td, {"column":'7'}).get_text()
        total = proc_tab.find_element(locator.supplychainmanagement.developer.td, {"column":'8'}).get_text()
        for idx,item in data.iterrows():
            if item[0] == state:
                agent = item[1]
                break
        date_elements[i].set_text(ship_date)
        total_elements[i].set_text(total[1:].strip())
        agent_elements[i].select_item(agent)
    
    tab.find_element(locator.supplychainmanagement.developer.button_submitbutton).click()

if __name__ == "__main__":
    main()
