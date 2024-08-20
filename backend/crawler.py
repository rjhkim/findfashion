import requests
from bs4 import BeautifulSoup

start_url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=shoes&_sacat=0&_pgn=2'


def crawl(url):
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('Given URL: "%s" is not available!' % url)
        return
    content = BeautifulSoup(response.text, 'lxml')

    links = content.findAll('div', {'class': 's-item__wrapper clearfix'})

    #get the image
    image = content.findAll('div', {'class': 's-item__image-wrapper'})

    #&_ipg=120 changes number of page results to 120, 60 by default

    #data: get product image, unique ID, name, link

    #data: pricing data: 


    #printing out link and item info
    for link in links:

        href_link = link.find('a', {'class': 's-item__link'})

        # prints link
        print(href_link['href'])

        # get image
        img_outer = link.find('div', {'class': 's-item__image-wrapper image-treatment'})

        img_tag = img_outer.find('img')

        img_link = img_tag['src']

        print(img_link)
        
        # print item name
        item_name_outer = link.find('div', {'class': 's-item__title'})

        spanner = item_name_outer.find('span')

        items = spanner.get_text()

        print(items)

        # get the price 
        price_outer = link.find('div', {'class': 's-item__detail s-item__detail--primary'})

        spanner2 = price_outer.find('span')

        price = spanner2.get_text()

        print(price)


crawl(start_url)


