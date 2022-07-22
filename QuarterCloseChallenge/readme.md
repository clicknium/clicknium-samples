# Clicknium automation sample solution - Finance Quarter Close

For many enterprises, at the end of each fiscal quarter, the finance team spends much time to make sure all of the financial obligations that were met.
This is a sample of financial qutarter close solution through [clicknium](https://www.clicknium.com/) automation.
It can review transactions automatically.
The detail of problem is: go through transactions in local financial system, and find the matching transaction in Bank system. If a match is found, need change the `Transaction Status` to `Verified` in local financial system.

The manual steps are as the following:
- login to local financial system.
- Query the transactions of this quarter.
- login bank system.
- For each transaction:
  - based on `Payment Account`, navigate to corresponding page.
  - search 'Payment Amount'.
  - If find the matched one, go back to local financial system, set the `Transaction Status` to Verified.
- After all transactions reviewed, click `Submit` button on local financial system.

# Run this sample
- follow [clicknium getting started](https://www.clicknium.com/documents) to set up develop environment.
- clone [sample repo](https://github.com/clicknium/clicknium-samples).
```
git clone https://github.com/clicknium/clicknium-samples.git
```
- open the folder 'QuarterCloseChallenge' in Visual Studio code
- open `app.py` in visual studio code.
- press `F5` to debug the sample or press `CTRL+F5` to run sample.
You will see the result:

![result](img/result.png)

# What the sample do
- open local financial system, get the transaction count and scrape `Amount` and `Account` information for each transaction.

```python
def get_transaction_count():
    transaction = []
    tab = cc.edge.open("https://developer.automationanywhere.com/challenges/automationanywherelabs-quarterclose.html", is_wait_complete=True, timeout=60)
    if tab.is_existing(locator.quaterclose.developer.button_onetrust_accept_btn_handler):
        tab.find_element(locator.quaterclose.developer.button_onetrust_accept_btn_handler).click()
    elems1 = tab.find_elements(locator.quaterclose.developer.text_paymentaccount)
    elems2 = tab.find_elements(locator.quaterclose.developer.text_paymentamount)
    count = len(elems1)
    for i in range(count):
        account = elems1[i].get_text()
        amount = elems2[i].get_text()
        transaction.append({"Amount":amount, "Account":account, "Status":"Unverified"})
    return tab,transaction
```

Here we leverage clicknium `find_elements` api, it can find all similar elements. For example, for PO number element's locator:

![locator1](img/locator1.png)

To record similar elements, you can click `Similar elements` on Clicknium Recorder:
![recorder1](img/recorder1.png)

The wizard will be shown:
![recorder2](img/recorder2.png)

You can record (`Ctrl`+click) two or more elements, for example:
![recorder3](img/recorder3.png)

It will show how many elements matched:
![recorder4](img/recorder4.png)

- open bank system and login
- iterate the transactions, based on each transaction's account, go to the corresponding account page
- search the transaction's amount, if find matched one, then mark the tranaction state to Verified.

```python
def validate_transaction(transaction):
    bank_tab = cc.edge.open("https://developer.automationanywhere.com/challenges/automationanywherelabs-arcadiabanklogin.html", is_wait_complete=True, timeout=60)
    bank_tab.find_element(locator.quaterclose.developer.email_inputemail).set_text("tammy.peters@petersmfg.com")
    bank_tab.find_element(locator.quaterclose.developer.password_inputpassword).set_text("arcadiabank!")
    bank_tab.find_element(locator.quaterclose.developer.a_login).click()
    for item in transaction:
        bank_tab.find_element(locator.quaterclose.developer.a_action, {"account":item["Account"]}).click()
        bank_tab.wait_appear(locator.quaterclose.developer.table1)
        bank_tab.find_element(locator.quaterclose.developer.text).set_text(item["Amount"])
        if bank_tab.is_existing(locator.quaterclose.developer.td_amount, {"amount":item["Amount"]}):
            item["Status"] = "Verified"
    bank_tab.close()
```

- go back to local financial system, batch update transactions state.

```python
def update_transaction_status(tab: BrowserTab, transaction):
    elems = tab.find_elements(locator.quaterclose.developer.select_status)
    count = len(elems)
    for i in range(count):
        elems[i].select_item(transaction[i]["Status"])

    tab.find_element(locator.quaterclose.developer.button_submitbutton).click()
```

# Locator
[Locator](https://www.clicknium.com/documents/automation/locator) is the identifier of UI element, through [clicknium vs code extension](https://marketplace.visualstudio.com/items?itemName=ClickCorp.clicknium) can record/edit the locator.

# Compare with Playwright
- To get silimar elements, I need write xpath by myself.
```python
elems1 = page.query_selector_all("//*[contains(@id,'PaymentAccount')]")
elems2 = page.query_selector_all("//*[contains(@id,'PaymentAmount')]")
```
- To search the transaction item, besides filling the text, I also need press the Enter.
```python
bank_page.locator("[placeholder=\"Search\\.\\.\\.\"]").fill(item["Amount"])
bank_page.press("[placeholder=\"Search\\.\\.\\.\"]",'Enter')
```

# More samples
You can find more automatin sample/solution from [clicknium github samples](https://github.com/clicknium/clicknium-samples)


