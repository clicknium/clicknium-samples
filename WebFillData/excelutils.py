import pandas

def read_excel(excel_file:str, sheet_name: str = 'Sheet1'):
    excel_date_df = pandas.read_excel(excel_file, sheet_name)
    excel_date_df = excel_date_df.where(excel_date_df.notnull(), None)
    dicts = excel_date_df.to_dict(orient='records')
    return dicts