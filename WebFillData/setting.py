import json

class Setting(object):
         
    with open("setting.json") as f:
        data = json.load(f)

    excel_file = data['excel_file']

    sheet_name = data['sheet_name']