#! python3
# Opens several Google search results.

import requests
import webbrowser
import bs4
import sys

print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))

res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))