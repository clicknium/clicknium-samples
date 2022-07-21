# Clicknium automation sample solution - Supply chain management

This is a sample of supply chain solution through [clicknium](https://www.clicknium.com/) web automation.
The detail of problem is: based on PO number, find and capture data from another `Purchase Order Tracking` web app, and look up state for agent from one excel, finally fill the data to PO management web portal.
The manual steps are as the following:
- download excel from PO management portal.
- copy PO number from web portal.
- login and query PO data based on PO number.
- look up the agent info from excel based on state.
- fill the PO data into PO management portal.


# Run this sample
- follow [clicknium getting started](https://www.clicknium.com/documents) to set up develop environment.
- clone [sample repo](https://github.com/clicknium/clicknium-samples).
```
git clone https://github.com/clicknium/clicknium-samples.git
```
- open the folder 'SupplyChainManagement' in Visual Studio code
- through `pip` install the dependenct packages
  
`requests` is used to download the CSV file and `pandas` is used to read CSV file.

```
pip install requests
pip install pandas
```
- open `app.py` in visual studio code.
- press `F5` to debug the sample or press `CTRL+F5` to run sample.
You will see the result:

![result](img/result.png)

# What the sample do
- open PO management portal, and capture the url of the excel to be downloaded.
- through `requests` module to download excel file.
- through `pandas` module to load data from excel file. 

```python
tab = cc.edge.open("https://developer.automationanywhere.com/challenges/automationanywherelabs-supplychainmanagement.html")
url = tab.find_element(locator.supplychainmanagement.developer.a_downloadagentterritoryspreadsheet).get_property("href")
excelFile = requests.get(url)
temp_file = os.path.join(os.getcwd(), 'test.xlsx')
open(temp_file, 'wb').write(excelFile.content)
data = pd.read_excel(temp_file,header=1)
```

- open `Purchas Order Tracking` web app and login
  
```python
proc_tab = tab.browser.new_tab("https://developer.automationanywhere.com/challenges/AutomationAnywhereLabs-POTrackingLogin.html")
proc_tab.find_element(locator.supplychainmanagement.developer.email_inputemail).set_text('username')
proc_tab.find_element(locator.supplychainmanagement.developer.password_inputpassword).set_text('password')
proc_tab.find_element(locator.supplychainmanagement.developer.button_signin).click()
```
after browser opened, will return the edge tab/page.

- through clicknium web automaton, find all elements for each PO item: PO number, Ship date, Order total and Assigned agent.

```python
po_elements = tab.find_elements(locator.supplychainmanagement.developer.text_ponumber)
date_elements = tab.find_elements(locator.supplychainmanagement.developer.text_shipdate)
total_elements = tab.find_elements(locator.supplychainmanagement.developer.text_ordertotal)
agent_elements = tab.find_elements(locator.supplychainmanagement.developer.select_agent)
count = len(po_elements)
```

Here we leverage clicknium `find_elements` api, it can find all similar elements. For example, for PO number element's locator:

![locator1](img/locator1.png)

we set the value of id to `PONumber*`, it will match all elements with id start with `PONumber`.

- iterate each PO number elements: capture PO number, query data from `Purchas Order Tracking` web app, fill the data in web portal and submit finally

```python
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
```

To get text of `state`, `ship_date` and `total`, we use [parametric locator](https://www.clicknium.com/documents/automation/parametric_locator), during running, specified the parameter value, so we can use one locator to locate several elements.

![parametric locator](img/parametric_locator.png)


# Locator
[Locator](https://www.clicknium.com/documents/automation/locator) is the identifier of UI element, through [clicknium vs code extension](https://marketplace.visualstudio.com/items?itemName=ClickCorp.clicknium) can record/edit the locator.

# More samples
You can find more automatin sample/solution from [clicknium github samples](https://github.com/clicknium/clicknium-samples)


