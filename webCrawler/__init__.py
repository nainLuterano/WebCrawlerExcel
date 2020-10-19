import requests
from bs4 import BeautifulSoup


class webCrawler:
    
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        self.soup = ''

    def setUrl(self, url):
        self.url = url

    def setHeaders(self, headers):
        self.headers = headers



    
    def getTags(self, tag):
        return self.soup.findAll(tag)
    
    def getTagsByClass(self, tag, classes):
        return self.soup.findAll(tag, classes)
        
    def getFindById(self, id):
        return self.soup.find(id=id)

    def download(self):
        response = requests.get(self.url, headers=self.headers)
        content = str(response.content)
        self.soup = BeautifulSoup(content, 'html.parser')  