import requests
from bs4 import BeautifulSoup
import sys

site_address= str(sys.argv[1])
request =requests.get("{}".format(site_address))

content =request.content
soup=BeautifulSoup(content,"html.parser")

element=soup.find_all("p",{"class":"verse"})
for i in element:
    print(i.text)
