from clicknium import clicknium, ui, locator

# Input
year = '2010'
mouth = 'Jan'
day = '1'

# The month corresponding to the date control
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Open the page
tab = clicknium.chrome.open("https://ant.design/components/date-picker/")

# Click the date input
tab.find_element(locator.chrome.ant.text).mouse_down()

# Compare the year. If not same, adjust to the next year or last year by clicking the button until they are same.
locator_year = ui(locator.chrome.ant.button_year)
current_year = locator_year.get_property(name="sInfo")

while year != current_year:
    if year > current_year:
        ui(locator.chrome.ant.button_year_next).click()
    else:
        ui(locator.chrome.ant.button_year_pre).click()
    current_year = locator_year.get_property(name="sInfo")

# Compare the month. If not same, adjust to the next month or last month by clicking the button until they are same.
locator_mouth = ui(locator.chrome.ant.button_mouth)
current_mouth = locator_mouth.get_property(name="sInfo")
current_mouth_index = months.index(current_mouth)
mouth_index = months.index(mouth)

while current_mouth_index != mouth_index:
    if mouth_index > current_mouth_index:
        ui(locator.chrome.ant.button_mouth_next).click()
    else:
        ui(locator.chrome.ant.button_mouth_pre).click()
    current_mouth = locator_mouth.get_property(name="sInfo")
    current_mouth_index = months.index(current_mouth)

# locate the date element with the date variable and click it
ui(locator.chrome.ant.div_day, {"day": day }).click()