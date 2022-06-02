# https://ned.ipac.caltech.edu/cgi-bin/imgdata?objname=NGC+7721&hconst=73.0&omegam=0.27&omegav=0.73&corr_z=1
import pandas as pd
import requests
from bs4 import BeautifulSoup

df = pd.read_excel("../RSAPending.xlsx")
for i in df["Galaxy"]:
    i = str(i)
    if("NGC" in i):
        print(f"{i[0:3]}+{i[3:]}")
        ext = i[3:]
        param = f"{i[0:3]}+{i[3:]}"
        page = requests.get(f"https://ned.ipac.caltech.edu/cgi-bin/imgdata?objname={param}&hconst=73.0&omegam=0.27&omegav=0.73&corr_z=1")
        souped = BeautifulSoup (page.content, "html.parser")
        imgs = souped.find_all("img")
        i=0
        for img in imgs:
            imglink = img.attrs.get("src")
            imglink = "https://ned.ipac.caltech.edu"+imglink
            filename = f"../RSA_images/NGC{ext}_{i}.jpg"
            print(filename)
            i+=1
            image = requests.get(imglink).content
            with open(filename, "wb") as file:
                file.write(image)