import sys
import os
import re
import requests
import  urllib.parse
from bs4 import BeautifulSoup

def cache(src):
    
    # preprocessing
    images = []
    if not os.path.exists('cache'):
        os.mkdir('cache')
    os.chdir('cache')
    r = requests.get(src, verify=False)
    soup = BeautifulSoup(r.text)
    p = re.compile('(url\()(([^\)]+)|(\"[^\"]+\")|(\'[^\']\'))(\))')
    os.system('clear')    
    print('PROCESSING...')
    print()

    # handling HTML
    imgs = soup.select('img')
    for img in imgs:
        url = img.get('src')
        save(abs(url, src), images)

    # handling internal CSS
    imgs = p.findall(r.text)
    for img in imgs:
        save(abs(img[2], src), images)
    
    # handling external CSS
    csss = soup.select('link[rel=stylesheet]')
    for css in csss:
        url = css.get('href')
        url = abs(url, src)
        r = requests.get(url, verify=False)
        imgs = p.findall(r.text)
        for img in imgs:
            save(abs(img[2], url), images)
    
    os.chdir('..')
    print()
    print('ALL DONE !')
    print()

def save(url, images):
    ext = url[url.rfind('.')+1:]
    if ext in ['png','ico','svg','jpg','jpeg','gif']:
        fileName = url[url.rfind('/')+1:]
        if fileName not in images:
            images.append(fileName)
            if os.path.isfile(fileName):
                print('>>> Skipping ' + fileName)
            else:
                try:
                    dat = requests.get(url, verify=False)
                    f = open(fileName, 'w+b')
                    print('>>> Saving ' + fileName)
                    f.write(dat.content)
                    f.close()
                except KeyboardInterrupt:
                    print()
                    print('Exiting...')
                    print()
                    sys.exit(0)
                except:
                    pass

def abs(url, src):
    url = urllib.parse.urljoin(src, url)
    return url

if __name__ == '__main__':
    cache(*sys.argv[1:])