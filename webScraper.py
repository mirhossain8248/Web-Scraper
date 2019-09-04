'''
Project Description:
This program scrapes any page from Newegg and retrives the following information
Brand, Title, Shipping
'''

'''
Things to improve on:
-Figure out formatting price
    Have figured out where the price is located on the page HTML but when
    I add price, it ruins the format of the excel file :(

-Scrape Multiple Pages
    As of right now this program only retrives the information from the first
    page. I will have to look further into the BeautifulSoup library or research
    this and will add it at a later date.
'''
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38"

uClient = uReq(my_url) #get the url
page_html = uClient.read() #read the url
uClient.close() #close url

page_soup = soup(page_html, 'html.parser') #parse html

'''
All the data that I need is stored within the class item container
on Neweggs website. Everything above item container was just the bannner,
search engine, and catagory lists. When using findAll, the program is searching
item-container
'''
containers = page_soup.findAll('div', {"class":"item-container"})

#Create a file to export data to
csv_file_export = open('product_info2.csv', 'w')
#csv_file_export.write('brand, product_name, shipping_price, item_price \n')
csv_file_export.write('brand, product_name, shipping_price \n')

'''
All of this was retrived from going on the page and inspecting HTML.
Note: only have to use the find function multiple times when the information I
want is nested. Used exception handing in the off chance that this information
would not be avaiable(this is just to make sure my entire program does not break)
'''
for itemContainer in containers:
    try:
        brand = itemContainer.find('div', 'item-info').find('div', 'item-branding').a.img["title"]
        title = itemContainer.find('a', class_ = 'item-title').text
        shipping_price = itemContainer.find('li', {'class':'price-ship'}).text.strip()
        #item_price = container.find('li', {'class':'price-current'}).text.strip()

    except Exception:
        brand = 'Brand not specified'
        title = 'Title not specified'
        shipping_price = 'Shipping price not specified'
        #item_price = "Item price not specified"

    #write all the data to the excel folder
    #csv_file_export.write(brand + ',' + title.replace(',', '|') + ',' +  shipping_price + ',' + item_price + '\n')
    csv_file_export.write(brand + ',' + title.replace(',', '|') + ',' +  shipping_price + '\n')
