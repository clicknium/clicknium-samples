

import os
import requests
import shutil
from clicknium import clicknium as cc, locator, ui
tab = cc.edge.attach_by_title_url(url = "https://gallerydemo.com/pages/outerwear")

imgs = tab.find_elements(locator.msedge.gallerydept.img_out)
titles = tab.find_elements(locator.msedge.gallerydept.span_out)

# iterate every image element
for x in range(len(imgs)):
    src = imgs[x].get_property("src")
    tstr = titles[x].get_text()

# download image with url and save to folder with title as name
    res = requests.get("https:"+src, stream = True)
    if res.status_code == 200:
        file = "c:\\test\\gallery\\" + tstr + ".png"
# use different name if the title is duplicated
        if(os.path.exists(file)):
            file = "c:\\test\\gallery\\" + tstr + str(x) + ".png"
        with open(file,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ',tstr)
    else:
        print('Image Couldn\'t be retrieved')


