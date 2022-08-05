from clicknium import clicknium, ui, locator

clicknium.chrome.open("https://jqueryui.com/datepicker/#date-range")

ui(locator.chrome.jqueryui.text_from).set_focus()
ui(locator.chrome.jqueryui.select_from).select_item("Jan")
ui(locator.chrome.jqueryui.a_1_from).click()

ui(locator.chrome.jqueryui.text_to).set_focus()
ui(locator.chrome.jqueryui.select_to).select_item("Dec")
ui(locator.chrome.jqueryui.a_31_to).click()