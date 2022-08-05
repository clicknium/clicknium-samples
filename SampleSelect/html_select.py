from clicknium import clicknium, ui, locator

clicknium.chrome.open("https://www.w3docs.com/learn-html/html-select-tag.html")
ui(locator.chrome.w3docs.select).select_item("Git")

