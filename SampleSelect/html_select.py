from clicknium import clicknium, ui, locator

tab = clicknium.chrome.open("https://www.w3docs.com/learn-html/html-select-tag.html")
tab.find_element(locator.chrome.w3docs.select).select_item("Git")

