import re
import threading
from queue import Queue
from html.parser import HTMLParser
from urllib import parse
from urllib.request import urlopen

class LinkFinder(HTMLParser):
    def __init__(self,page_url):
        super().__init__()
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self,tag,attrs):
        if tag == 'a':
            for (attribute,value) in attrs:
                if attribute == 'href':
                    pattern = r'^https://www[.]youtube[.]com/watch[?].*$'
                    if(re.findall(pattern,value)):
                        self.links.add(value)

    def page_links(self):
        return self.links

    def error(self, message):
        pass
    
    
    
def gather_links(page_url):
    html_string=''
    try:
        response = urlopen(page_url)
        if 'text/html' in response.getheader('Content-Type'):
            html_bytes = response.read()
            html_string = html_bytes.decode('utf-8')
        finder=LinkFinder(page_url)
        finder.feed(html_string)
    except Exception as e:
        print(str(e))
        return set()
    return finder.page_links()

#for i in crawl_url:
#    print(gather_links(i))
links=[]
NO_OF_THREADS= 4
queue = Queue()

def create_workers():

    for _ in range(NO_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()
    return links

    
def work():
    while True:
      
        url = queue.get()
        links.append(gather_links(url))
        queue.task_done()


def create_jobs(urls):
    for link in urls:
        queue.put(link)
    queue.join()

    


def crawl(urls):
    if urls:
        create_jobs(urls)

def rem_links():
    global links
    links = []