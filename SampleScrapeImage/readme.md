# [Clicknium-scrape-image]How to scrape images from the website

## Introduction
It is a common requirement of scraping images from the website by Python.  
It isn't just a tool for sharpening your programming skills.  
Take an example of scraping the images from [Clicknium website](https://www.clicknium.com)
Learn how to scrape images from any website using Clicknium.

- Notes: More about the installation and the tutorial of Clicknium Automation, please refer to [here](https://www.clicknium.com/documents).

## How to Scrape the images?
1. With the Clicknium recorder, record an image from Clicknium website.
2. Change the locator of the image. Here we drop the other property options and keep the tag only for general use.
![record](./img/clicknium-img.png) 
3. When the locator is changed, we write the code as below.
   ```python
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
   ```
