# [Clicknium-calendar]如果通过自动化对日期选择框设值

## 引言
前端日期取值设值是自动化中比较常见的需求。但前端组件库较多，每种框架都有所不同，那我们来看看clicknium是如果实现多种前端UI框架中日期相关的操作。
- PS:Clicknium Automation安装基础使用参考 [官方文档](https://https://www.clicknium.com/documents)


## CalendarUI控件种类

### jQueryUI Calendar 
基于jQuery的UI库。[官方文档](https://jqueryui.com/datepicker/#date-range)

### Ant Design
基于React的UI库。[官方文档](https://ant.design/components/date-picker/) 


- ps: clicknium基于Web的录制除IE外需要按照浏览器插件。安装步骤参考 [Clicknium 浏览器插件](https://www.clicknium.com/documents/developtools/vscode/extensions/)

## How To Automate Calendar In Clicknium For Automation Testing?

### JqueryUI Calendar
1. 通过clicknium提供的录制器，录制页面中需要操作的组件元素。
   clicknium提供了非常强大的录制功能。  
   具体操作可参照 [Clicknium 录制器](https://www.clicknium.com/documents/developtools/vscode/extensions/)  
   这里我们录制内容如图。
![record](./img/jquery-record.png)  
   to参考from也录制这三部分。

2. 修改日期locator。因为自动录制是按照日期所在table的行列生成的，每个月日期对应的行列有所不同，不能准确定位。这里我们将日期元素修改成根据sinfo和index来定位。  
   修改前:
   ![before](./img/jquery-update-before.png) 
   修改后：
   ![record](./img/jquery-update-after.png) 
3. 准备工作做好后，我们可以上代码了。
   ```python
   from clicknium import clicknium, ui, locator

   clicknium.chrome.open("https://jqueryui.com/datepicker/#date-range")

   ui(locator.chrome.jqueryui.text_from).set_focus()
   ui(locator.chrome.jqueryui.select_from).select_item("Jan")
   ui(locator.chrome.jqueryui.a_1_from).click()

   ui(locator.chrome.jqueryui.text_to).set_focus()
   ui(locator.chrome.jqueryui.select_to).select_item("Dec")
   ui(locator.chrome.jqueryui.a_31_to).click()
   ```

### Ant Design
1. 思路：  
   点击输入框，弹出日期选择popup。  
   比较输入值的年是否一致，不一致通过上一年下一年，进行调整。月份同理。  
   年月一致后，找到对应天的元素，最后点击此元素。
1. 通过clicknium提供的录制器，录制页面中需要操作的组件元素。  
   录制元素如图。
   ![record](./img/ant-record.png) 
2. 修改text.locator,因为页面中有多个Examples，这里勾上index。  
   修改年月、日对应的locator。年月把sInfo定位换成class属性来定位。日的sInfo换成变量day。
   修改后
   ![year](./img/ant-year.png) 
   ![before](./img/ant-month.png) 
   ![before](./img/ant-day.png) 
3. 上代码
   
   ```python
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
   ```
