# How to read data from excel and fill data on the web page

## Setup

1. System requirements

- Windows 7 SP1 or above, windows 10 or 11 is recommended
- Python 3.7 or above.

2. Install the dependencies needed to run the sample

```
pip install -r requirements.txt
```

or 

```
pip install clicknium
pip install pandas
```

3. Install Clicknium Edge extension, refer to [Edge Extension](https://www.clicknium.com/documents/developtools/vscode/extensions/edgeextension) for more information

```
from clicknium import clicknium as cc
cc.edge.extension.install()
```

## How to run

1. Modify configuration file 'setting.json' to update the content with your information
```
{
    "excel_file": "D:\\test\\forms\\test.xlsx",
    "sheet_name": "jobs"
}
```
2. Run the sample
```
python sample.py
```