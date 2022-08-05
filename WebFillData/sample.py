from clicknium import clicknium as cc, locator
from excelutils import read_excel
from setting import Setting


def fill_single_record(record):
    _tab.find_element(locator.edge.forms.title).set_text(record['Job Title'] if record['Job Title'] else "")
    _tab.find_element(locator.edge.forms.company_name).set_text(record['Company Name'] if record['Company Name'] else "")
    _tab.find_element(locator.edge.forms.company_size).set_text(record['Company Size'] if record['Company Size'] else "")
    _tab.find_element(locator.edge.forms.type).set_text(record['Job Type'] if record['Job Type'] else "")
    _tab.find_element(locator.edge.forms.post_date).set_text(record['Post Date'] if record['Post Date'] else "")
    _tab.find_element(locator.edge.forms.link).set_text(record['Job Link'] if record['Job Link'] else "")
    _tab.find_element(locator.edge.forms.submit).click()
    _tab.wait_appear(locator.edge.forms.submitanother, wait_timeout=5).click()


if __name__ == "__main__":
    records = read_excel(Setting.excel_file, Setting.sheet_name)
    _tab = cc.edge.open("https://forms.office.com/r/contoso")
    for record in records:
        fill_single_record(record)
    _tab.close()