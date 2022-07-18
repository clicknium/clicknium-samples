# Sample to demostrate clicknium combined automation for desktop and web application

This is a sample to solve data migration problem through [clicknium]((https://www.clickcorp.com/?source=github)) desktop&web automation.
The detail of problem is: migrate employee data from a legacy thick client application into new HR system.
The manual steps are as the following:
- query data from legacy client app based on employee id.
- query more meta data of employee through internal rest API.
- fill the data of employee to the new HR system(web portal).


# run this sample
- follow [clicknium getting started](https://www.clickcorp.com/documents?source=github) to set up develop environment.
- clone this sample repo.
- download and unzip [legacy thick client app](https://github.com/AutomationAnywhere/Employee-Data-Migration/raw/master/EmployeeList.zip) to local repo folder.
- open `app.py` in visual studio code.
- press `F5` to debug the sample or press `CTRL+F5` to run sample.

# what the sample do
- open the legacy client application through subprocess module, it will be used to query data later.

```
current_dir = os.path.dirname(os.path.abspath(__file__))
employeeList_exe = os.path.join(current_dir, "EmployeeList.exe")
process = subprocess.Popen(employeeList_exe)
```

- through clicknium python module to open browser, open new HR system, the sample uses microsoft edge browser.
  
```
tab = cc.edge.open("https://developer.automationanywhere.com/challenges/automationanywherelabs-employeedatamigration.html")
```
after browser is opened, will return the edge tab/page.

- through clicknium web automaton, get the employee id in new HR system.

```
employee_id = tab.find_element(locator.employeedatamigration.developer.text_employeeid).get_text()
```

-  based the captured employee_id above, through clicknium desktop automation, find the enployee information on legacy client application.

```
cc.ui(locator.employeedatamigration.employee.edit_txtempid).set_text(employee_id)
cc.ui(locator.employeedatamigration.employee.button_btnsearch).click()
item["first_name"] = cc.ui(locator.employeedatamigration.employee.edit_txtfirstname).get_text()
item["last_name"] = cc.ui(locator.employeedatamigration.employee.edit_txtlastname).get_text()
item["email_id"] = cc.ui(locator.employeedatamigration.employee.edit_txtemailid).get_text()
item["city"] = cc.ui(locator.employeedatamigration.employee.edit_txtcity).get_text()
... ...
```

automatically set text for employee_id, then click search button, finally capture all information such as first_name, last_name etc of this emplyee.

- through `requests` module, send http request to get the extra informaton(phone number, start date) about the employee.

```
response = requests.get(api_url + employee_id)
print(datetime.datetime.now().strftime("%H:%M:%S") + " get response")
obj = json.loads(response.content.decode('UTF-8'))
item["phoneNumber"] = obj["phoneNumber"]
item["startDate"] = obj["startDate"]
```

- fill the data into new HR system through clicknium web automation.

# Locator
[Locator](https://www.clickcorp.com/documents#automation/locator) is the identifier of UI element, through [clicknium vs code extension](https://marketplace.visualstudio.com/items?itemName=ClickCorp.clicknium) can record/edit the locator.


