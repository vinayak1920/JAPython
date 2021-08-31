import requests

from bs4 import BeautifulSoup

url = input('Input the URL:\n')
r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})

show = {}
if r and 'title' in url:
    try:
        soup = BeautifulSoup(r.content, 'html.parser')
        show['title'] = soup.find('title').text
        show['description'] = soup.find('meta', {'name': 'description'})['content']
    except KeyError:
        print('Invalid quote resource!')
    else:
        print(show)
else:
    print('Invalid movie page!')
