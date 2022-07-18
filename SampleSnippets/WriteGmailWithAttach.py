from clicknium import clicknium as cc, locator, ui

browsers = cc.chrome.browsers
print("{} chrome windows are opened".format(len(browsers)))
for chrome in browsers:
    tabs = chrome.tabs
    print("{} chrome tabs are opened in one browser".format(len(tabs)))
    for tab in tabs:
        print("tab title:{}, url:{}".format(tab.title, tab.url))
