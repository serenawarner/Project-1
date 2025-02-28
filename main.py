import re
import pytest

class URLs:
    def __init__(self):
        self.links = {}
        self.count = 0

    def shorten(self,URL):
        url =  "https://link.com/s" + str(self.count)
        self.count+=1
        return url

    def store(self,URL):
        self.links[URL] = self.shorten(URL)

    def printShorten(self,URL):
        print(self.links[URL])

    def printURLs(self):
        print(self.links)
        return self.links

    def getCount(self):
        return self.count
    
    def findShortened(self, search):
        for key, val in self.links.items():
            if val == search:
                return key
        return None

    def validate(self,URL):        
        x = re.search("https://.*\\..*/.*", URL)
        if x == None:
            return False
        return True


def run(state, url):
    if(state == "0"):
        link = input("Please input your link: ")
        x = url.validate(link)
        if(x):
            url.store(link)
            return True
        else:
            print("Invalid link")
            return False
    if(state == "1"):
        link = input("Please input your link: ")
        x = url.validate(link)
        if(x):
            url.store(link)
            url.printShorten(link)
            return True
        else:
            print("Invalid link")
            return False
    if(state == "2"):
        url.printURLs()
        return url.printURLs()
    if(state == "3"):
        print(url.getCount())
        return url.getCount()
    if(state == "4"):
        shortLink = input("Please input a shortened link: ")
        longLink = url.findShortened(shortLink)
        if longLink == None:
            return None
        print(longLink)
        return longLink

state = "0"

url = URLs()
'''
while(state != "00"):
    print("Would you like to: \n   (0) Store a URL\n   (1) Store and return a shortened URL\n   (2) List stored URLs\n   (3) Display number of stored URLs\n   (4) Return a full URL from a shortened input\n")
    state = input()
    run(state,url)
    print("-------------------------------------------------------------------------------------------")
'''

# TESTS

def test0True(monkeypatch):
    state = "0"
    urlTest = URLs()
    monkeypatch.setattr('builtins.input', lambda _: "https://www.hottogo.com/")
    assert run(state,urlTest) == True
    
def test0False(monkeypatch):
    state = "0"
    urlTest = URLs()
    monkeypatch.setattr('builtins.input', lambda _: "https://www.hottogo")
    assert run(state,urlTest) == False

def test1True(monkeypatch):
    state = "1"
    urlTest = URLs()
    monkeypatch.setattr('builtins.input', lambda _: "https://www.hottogo.com/")
    assert run(state,urlTest) == True

def test1False(monkeypatch):
    state = "1"
    urlTest = URLs()
    monkeypatch.setattr('builtins.input', lambda _: "https://www.hott")
    assert run(state,urlTest) == False

def test2(monkeypatch):
    urlTest = URLs()
    state = "0"
    monkeypatch.setattr('builtins.input', lambda _: "https://www.hotto.go/")
    run(state,urlTest)
    monkeypatch.setattr('builtins.input', lambda _: "https://this.shouldn't.work.lol")
    run(state,urlTest)
    
    state = "2"
    print(run(state,urlTest))
    assert run(state,urlTest) == {'https://www.hotto.go/': 'https://link.com/s0'}

def test3(monkeypatch):
    urlTest = URLs()
    state = "0"
    monkeypatch.setattr('builtins.input', lambda _: "https://www.hotto.go/")
    run(state,urlTest)
    monkeypatch.setattr('builtins.input', lambda _: "https://this.shouldn't.work.lol")
    run(state,urlTest)
    monkeypatch.setattr('builtins.input', lambda _: "https://this.should.work/")
    run(state,urlTest)

    state = "3"

    assert run(state,urlTest) == 2

def test4True(monkeypatch):
    urlTest = URLs()
    state = "0"
    monkeypatch.setattr('builtins.input', lambda _: "https://www.hotto.go/")
    run(state,urlTest)
    state = "4"
    monkeypatch.setattr('builtins.input', lambda _: "https://link.com/s0")
    
    assert run(state, urlTest) == "https://www.hotto.go/"

def test4False(monkeypatch):
    urlTest = URLs()
    state = "0"
    monkeypatch.setattr('builtins.input', lambda _: "https://www.hotto.go/")
    run(state,urlTest)
    state = "4"
    monkeypatch.setattr('builtins.input', lambda _: "https://link.com/s1")
    
    assert run(state, urlTest) == None