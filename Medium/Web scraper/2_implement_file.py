show = {}
if r:  # and 'title' in url:
    '''try:
        soup = BeautifulSoup(r.content, 'html.parser')
        show['title'] = soup.find('title').text
        show['description'] = soup.find('meta', {'name': 'description'})['content']
    except KeyError:
        print('Invalid quote resource!')
    else:
        print(show)
'''
    try:
        with open('source.html', 'wb') as f:
            f.write(r.content)
    except Exception:
        print(f'The URL returned {r.status_code}!')
    else:
        print('Content saved.')
else:
    print(f'The URL returned {r.status_code}')  # Invalid movie page!'
