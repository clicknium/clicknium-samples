import sqlite3
from time import sleep
import requests, os, csv
from clicknium import clicknium as cc, locator,ui

def query_and_fill_csv(card_data):
    cards = []
    conn = None
    try:
        conn = sqlite3.connect("CustomerData.db")
    except sqlite3.Error as e:
        print(e)
    sql = "SELECT c.id as id, d.first_name as first_name, d.last_name as last_name, c.card_number as card_number, c.cvv as cvv, c.brand as brand \
    FROM card_details as c inner join customer_details as d \
    where c.id=d.customer_id and c.level=\"{level}\" and c.expiration=\"{expiration}\" and c.card_type=\"{type}\" \
    and d.last_name=\"{last_name}\" and c.brand=\"{brand}\" and c.card_number like \"{id}%\""
    
    cols = ["CustomerID", "FirstName", "LastName", "CardNumber", "CVV", "CardBrand"]
    for item in card_data:
        cur = conn.cursor()
        cur.execute(sql.format(level=item['level'], expiration=item['expiration'], type=item['type'], last_name=item['last_name'], brand=item['brand'], id=item['id']))
        row = cur.fetchone()
        if row != None:
            cards.append([row[0], row[1], row[2], row[3], row[4], row[5]])

    with open('result.csv', 'w') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)

        write.writerow(cols)
        write.writerows(cards)

def main():
    tab = cc.chrome.open('https://developer.automationanywhere.com/challenges/automationanywherelabs-cyberlossprevention.html')
    tab.find_element(locator.chrome.developer.a_ryansclublogin).click()
    club_tab = cc.chrome.attach_by_title_url(url='https://developer.automationanywhere.com/challenges/automationanywherelabs-ryansclub*')
    club_tab.find_element(locator.chrome.developer.email_email).set_text('notthecyberteam@gmail.com')
    club_tab.find_element(locator.chrome.developer.password_password).set_text('letme!n')
    club_tab.find_element(locator.chrome.developer.button_login).click()
    elem_dumps = club_tab.find_element(locator.chrome.developer.a_creditcarddumps)
    #expanded = elem_dumps.get_property('aria-expanded')
    #if expanded == 'false':
    #    elem_dumps.click()
    club_tab.find_element(locator.chrome.developer.a_dump349473).click()
    club_tab.wait_appear(locator.chrome.developer.td, {'col':1})

    #download dbfile
    '''
    url = tab.find_element(locator.chrome.developer.a_customerdatabasedownload).get_property("href")
    dbFile = requests.get(url)
    temp_file = os.path.join(os.getcwd(), 'CustomerData.db')
    open(temp_file, 'wb').write(dbFile.content)

    url = tab.find_element(locator.chrome.developer.a_cancellationscsvtemplate).get_property("href")
    csvFile = requests.get(url)
    temp_file = os.path.join(os.getcwd(), 'cancel.csv')
    open(temp_file, 'wb').write(csvFile.content)
    '''
    
    card_data = []

    has_data = True
    while has_data:
        elems_num = club_tab.find_elements(locator.chrome.developer.td, {'col':1})
        elems_expiration = club_tab.find_elements(locator.chrome.developer.td, {'col':2})
        elems_level = club_tab.find_elements(locator.chrome.developer.td, {'col':3})
        elems_brand = club_tab.find_elements(locator.chrome.developer.td, {'col':4})
        elems_type = club_tab.find_elements(locator.chrome.developer.td, {'col':5})
        elems_last_name = club_tab.find_elements(locator.chrome.developer.td, {'col':6})

        count = len(elems_num)
        for idx in range(count):
            card_data.append({'id':elems_num[idx].get_text().replace('*',''),
            'expiration':elems_expiration[idx].get_text(),
            'level':elems_level[idx].get_text(),
            'brand':elems_brand[idx].get_text().strip(),
            'type':elems_type[idx].get_text(),
            'last_name':elems_last_name[idx].get_text()})
        if club_tab.is_existing(locator.chrome.developer.a):
            club_tab.find_element(locator.chrome.developer.a).click()
        else:
            has_data = False
    query_and_fill_csv(card_data)
 
    tab.find_element(locator.chrome.developer.file_filetoupload).click(by='mouse-emulation')
    ui(locator.chrome.edit_1148).set_text(os.path.join(os.getcwd(), 'result.csv'), by='set-text')
    ui(locator.chrome.button_1).click(by='control-invocation')
    sleep(2)
    tab.find_element(locator.chrome.developer.button_btnuploadfile).click()

if __name__ == "__main__":
    main()