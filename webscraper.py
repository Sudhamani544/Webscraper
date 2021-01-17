import requests
from bs4 import BeautifulSoup
import pprint

res= requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text,'html.parser')
link = soup.select('.storylink')
votes = soup.select('.subtext')
nextpage = soup.select('.morelink')
hn = []

def sort_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse = True)

def create_custom_hn(link,votes):
    for index,url in enumerate(link):
        href = url.get('href')
        title = url.getText()
        vote = votes[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 99:
                hn.append({'link' : href, 'title' : title, 'votes' : points})
    if nextpage[0].get('href') == 'news?p=2':
        print(nextpage[0].get('href'))
        # nextpage[0].click()
        # create_custom_hn(link,votes)
    return sort_by_votes(hn)

pprint.pprint(create_custom_hn(link,votes))
