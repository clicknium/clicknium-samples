import json
import subprocess,os
from clicknium import clicknium as cc, locator
from clicknium.core.models.web.browser import BrowserTab
import requests
import requests, datetime

def submit_item(tab:BrowserTab, item):
    tab.find_element(locator.employeedatamigration.developer.text_firstname).set_text(item["first_name"])
    tab.find_element(locator.employeedatamigration.developer.text_lastname).set_text(item["last_name"])
    tab.find_element(locator.employeedatamigration.developer.text_phone).set_text(item["phoneNumber"])
    tab.find_element(locator.employeedatamigration.developer.text_email).set_text(item["email_id"])
    tab.find_element(locator.employeedatamigration.developer.text_city).set_text(item["city"])
    tab.find_element(locator.employeedatamigration.developer.text_zip).set_text(item["zip"])
    tab.find_element(locator.employeedatamigration.developer.text_title).set_text(item["job_title"])
    tab.find_element(locator.employeedatamigration.developer.text_startdate).set_text(item["startDate"])
    tab.find_element(locator.employeedatamigration.developer.text_manager).set_text(item["manager"])
    tab.find_element(locator.employeedatamigration.developer.select_state).select_item(item["state"])
    tab.find_element(locator.employeedatamigration.developer.select_department).select_item(item["department"])
    tab.find_element(locator.employeedatamigration.developer.button_submitbutton).click()

def main():
    api_url = "https://botgames-employee-data-migration-vwsrh7tyda-uc.a.run.app/employees?id="
    current_dir = os.path.dirname(os.path.abspath(__file__))
    employeeList_exe = os.path.join(current_dir, "EmployeeList.exe")
    process = subprocess.Popen(employeeList_exe)

    tab = cc.edge.open("https://developer.automationanywhere.com/challenges/automationanywherelabs-employeedatamigration.html")
    for _ in range(10):
        item = {}
        employee_id = tab.find_element(locator.employeedatamigration.developer.text_employeeid).get_text()
        cc.ui(locator.employeedatamigration.employee.edit_txtempid).set_text(employee_id)
        cc.ui(locator.employeedatamigration.employee.button_btnsearch).click()
        item["first_name"] = cc.ui(locator.employeedatamigration.employee.edit_txtfirstname).get_text()
        item["last_name"] = cc.ui(locator.employeedatamigration.employee.edit_txtlastname).get_text()
        item["email_id"] = cc.ui(locator.employeedatamigration.employee.edit_txtemailid).get_text()
        item["city"] = cc.ui(locator.employeedatamigration.employee.edit_txtcity).get_text()
        item["state"] = cc.ui(locator.employeedatamigration.employee.edit_txtstate).get_text()
        item["zip"] = cc.ui(locator.employeedatamigration.employee.edit_txtzip).get_text()
        item["job_title"] = cc.ui(locator.employeedatamigration.employee.edit_txtjobtitle).get_text()
        item["manager"] = cc.ui(locator.employeedatamigration.employee.edit_txtmanager).get_text()
        item["department"] = cc.ui(locator.employeedatamigration.employee.edit_txtdepartment).get_text()

        print(datetime.datetime.now().strftime("%H:%M:%S") + " send request")
        response = requests.get(api_url + employee_id)
        print(datetime.datetime.now().strftime("%H:%M:%S") + " get response")
        obj = json.loads(response.content.decode('UTF-8'))
        item["phoneNumber"] = obj["phoneNumber"]
        item["startDate"] = obj["startDate"]
        
        submit_item(tab, item)

    process.kill()
    tab.browser.close()

if __name__ == "__main__":
    main()