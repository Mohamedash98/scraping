import requests
import bs4

for item in range (150):
    url = f'https://www.etsy.com/c/clothing-and-shoes/mens?explicit=1&ref=pagination&page={item+1}'
    page = requests.get(url)
    content = page.content
    soup = bs4.BeautifulSoup(content, "html.parser")
    List = soup.find_all('li', {'class': 'wt-list-unstyled'})

    for item in List:
        print('name :', item.find('h3', {'class': 'wt-text-caption v2-listing-card__title wt-text-truncate'}).text)
        print('price = ', item.find('span', {'class': 'currency-value'}).text)
        print('\n\n\n')
