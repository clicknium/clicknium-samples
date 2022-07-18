import os
import sys
from time import sleep
from clicknium import clicknium as cc, locator
from clicknium.core.models.web.browser import BrowserTab

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

def update_transaction_status(tab: BrowserTab, transaction):
    elems = tab.find_elements(locator.quaterclose.developer.select_status)
    count = len(elems)
    for i in range(count):
        elems[i].select_item(transaction[i]["Status"])

    tab.find_element(locator.quaterclose.developer.button_submitbutton).click()
    #tab.find_element(locator.QuaterClose.developer.div).highlight()
    imagefile = os.path.join(os.path.dirname(__file__), 'result', 'result.png')
    tab.find_element(locator.quaterclose.developer.div).save_to_image(imagefile)

def validate_transaction(transaction):
    bank_tab = cc.edge.open("https://developer.automationanywhere.com/challenges/automationanywherelabs-arcadiabanklogin.html", is_wait_complete=True, timeout=60)
    bank_tab.find_element(locator.quaterclose.developer.email_inputemail).set_text("tammy.peters@petersmfg.com")
    bank_tab.find_element(locator.quaterclose.developer.password_inputpassword).set_text("arcadiabank!")
    bank_tab.find_element(locator.quaterclose.developer.a_login).click()
    for item in transaction:
        print(item["Account"])
        bank_tab.find_element(locator.quaterclose.developer.a_action, {"account":item["Account"]}).click()
        #sleep(1)
        #bank_tab.find_element(locator.chrome.developer.table1).highlight()
        bank_tab.wait_appear(locator.quaterclose.developer.table1)
        bank_tab.find_element(locator.quaterclose.developer.text).set_text(item["Amount"])
        #bank_tab.find_element(locator.chrome.developer.text).set_text(item["Amount"], input_method='keyboardsimulatewithclick')
        if bank_tab.is_existing(locator.quaterclose.developer.td_amount, {"amount":item["Amount"]}):
            item["Status"] = "Verified"
    bank_tab.close()

tab,transaction = get_transaction_count()
validate_transaction(transaction)
update_transaction_status(tab, transaction)
#tab.close()