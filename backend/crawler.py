import requests
from bs4 import BeautifulSoup

start_url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=shoes&_sacat=0'

response = requests.get(start_url)
content = BeautifulSoup(response.text, 'lxml')
links = content.findAll('a', {'class': 's-item__link'})

#get the image
image = content.findAll('div', )

#&_ipg=120 changes number of page results to 120, 60 by default

#data: get product image, unique ID, name, link

#data: pricing data: 


#printing out link and item info
for link in links:
    print(link['href'])

    title_div = link.find('div', {'class': 's-item__title'})

    if title_div:
        span_role = title_div.find('span', {'role': 'heading'})

        if span_role:
            #gets product name
            print(span_role.get_text())

