from clicknium import clicknium, ui, locator

tab = clicknium.chrome.open("https://jqueryui.com/datepicker/#date-range")

tab.find_element(locator.chrome.jqueryui.text_from).set_focus()
tab.find_element(locator.chrome.jqueryui.select_from).select_item("Jan")
tab.find_element(locator.chrome.jqueryui.a_1_from).click()

tab.find_element(locator.chrome.jqueryui.text_to).set_focus()
tab.find_element(locator.chrome.jqueryui.select_to).select_item("Dec")
tab.find_element(locator.chrome.jqueryui.a_31_to).click()