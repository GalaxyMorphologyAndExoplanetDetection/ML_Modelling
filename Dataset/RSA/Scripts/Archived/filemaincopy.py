# https://ned.ipac.caltech.edu/cgi-bin/imgdata?objname=NGC+7721&hconst=73.0&omegam=0.27&omegav=0.73&corr_z=1
import requests
from bs4 import BeautifulSoup
start = 2500
stop = 7797
stop = 3500
for j in range(start, stop):
    num = j
    page = requests.get(f"https://ned.ipac.caltech.edu/cgi-bin/imgdata?objname=NGC+{num}&hconst=73.0&omegam=0.27&omegav=0.73&corr_z=1")
    souped = BeautifulSoup (page.content, "html.parser")
    imgs = souped.find_all("img")
    i=0
    for img in imgs:
        imglink = img.attrs.get("src")
        imglink = "https://ned.ipac.caltech.edu"+imglink
        filename = f"../images/NGC{num}_{i}.jpg"
        print(filename)
        i+=1
        image = requests.get(imglink).content
        with open(filename, "wb") as file:
            file.write(image)
