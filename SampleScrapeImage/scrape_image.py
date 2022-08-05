from clicknium import clicknium, locator
import requests

websiteUrl = "https://www.clicknium.com"
tab = clicknium.chrome.open(websiteUrl)

imgs = clicknium.find_elements(locator.chrome.clicknium.img)

sources = []
for img in imgs:
   source = img.get_property("src")
   if source:
        sources.append(source)

for source in sources:
    webs = requests.get(websiteUrl + source)
    open('images/' + source.split('/')[-1], 'wb').write(webs.content)