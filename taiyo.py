from webbrowser import Chrome
import webbrowser
import requests
import subprocess
from bs4 import BeautifulSoup
url = "https://opentender.eu/start"
url2= "https://opentender.eu"
page = requests.get(url)
print (page)
soup = BeautifulSoup(page.content, 'html.parser')

# countries = soup.find_all('li', class_= "portal-link")
# print(countries)
country_link = []
download_link = []
for c in soup.find_all('li', class_= "portal-link"):
    for a in c.find_all('a', href=True):
        country_link.append(url2+a['href'])
        # download_link.append(url2+a['href']+'/download')
        # #print(url2+a['href'])

#print (download_link)
#print (country_link)

for i in country_link:
    page2 = requests.get(i)
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    for a in soup2.find_all('li'):
        for c in a.find_all('a', href = True, text = 'Download'):
            download_link.append(url2+c['href'])
            #print (c['href'])

#print (download_link)     

data_link = []
for i in download_link:
    page_final = requests.get(i)
    soup_final = BeautifulSoup(page_final.content, 'html.parser')
    link = soup_final.find('a', class_= "download-button", href = True)
    data_link.append(url2+link['href'])
    #print (link['href'])

#print (data_link)
download_list = []
download_list.append([data_link[i] for i in range(len(data_link)) if i%2 !=0])
# print (download_list)


for link in download_list[0]:
    webbrowser.open(link)