import os
from clicknium import clicknium as cc, locator, ui

tab = cc.edge.attach_by_title_url(url="https://mail.google.com/mail/*inbox")
tab.find_element(locator.msedge.mail.div_compose).click()
tab.find_element(locator.msedge.mail.textarea_vz).set_text("clicknium@clickcorp.com")
tab.find_element(locator.msedge.mail.text_wn).set_text("testing email")
tab.find_element(locator.msedge.mail.div_zz).click(by='mouse-emulation')

readme = os.path.join(os.getcwd(), 'readme.md')

cc.find_element(locator.msedge.mail.edit_1148).set_text(readme, by='set-text')
cc.find_element(locator.msedge.mail.button_1).click()

# click send button
#tab.find_element(locator.msedge.mail.div_sj).click()