from clicknium import clicknium, ui, locator

clicknium.chrome.open("https://ant.design/components/select/")

ui(locator.chrome.ant.select).click()
ui(locator.chrome.ant.option_jack).click()