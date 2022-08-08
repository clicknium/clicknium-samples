from clicknium import clicknium, ui, locator

tab = clicknium.chrome.open("https://ant.design/components/select/")

tab.find_element(locator.chrome.ant.select).click()
tab.find_element(locator.chrome.ant.option_jack).click()