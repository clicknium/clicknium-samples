from clicknium import clicknium, ui, locator

# 输入项
year = '2010'
mouth = 'Jan'
day = '1'

# 对应日期控件中月份常量
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# 打开页面
clicknium.chrome.open("https://ant.design/components/date-picker/")

# 点击日期输入框
ui(locator.chrome.ant.text).mouse_down()

# 比较年份是否一致，不一致的情况通过上一年，下一年按钮调整，直到一致
locator_year = ui(locator.chrome.ant.button_year)
current_year = locator_year.get_property(name="sInfo")

while year != current_year:
    if year > current_year:
        ui(locator.chrome.ant.button_year_next).click()
    else:
        ui(locator.chrome.ant.button_year_pre).click()
    current_year = locator_year.get_property(name="sInfo")

# 比较月份是否一致，不一致的情况通过上一月，下一月按钮调整，直到一致
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

# 用日期变量定位到对应的日期元素，并点击
ui(locator.chrome.ant.div_day, {"day": day }).click()