# multidownloadXkcd.py - Downloads XKCD comics using multiple threads.

import threading
import os
import bs4
import requests

os.makedirs('xkcd', exist_ok=True)


def downloadXkcd(start_comic, end_comic):
    for urlNumber in range(start_comic, end_comic):
        print('Downloading page http://xkcd.com/%s...' % urlNumber)
        res = requests.get('http://xkcd.com/%s' % urlNumber)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        comicElem = soup.select('#comic img')
        if not comicElem:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            print('Downloading image %s...' % comicUrl)
            res = requests.get(comicUrl)
            res.raise_for_status()

            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()


downloadThreads = []
for i in range(0, 1400, 100):
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 90))
    downloadThreads.append(downloadThread)
    downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
