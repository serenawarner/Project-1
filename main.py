class URLs:
    def __init__(self):
        self.links = {}
        self.count = 0

    def shorten(self,URL):
        url =  "https://myLink.com/short" + str(self.count)
        self.count+=1
        return url

    def store(self,URL):
        self.links[URL] = self.shorten(URL)

    def printShorten(self,URL):
        print(self.links[URL])

    def printURLs(self):
        print(self.links)

    def getCount(self):
        return self.count
    
    def findShortened(self, search): 
        for key, val in self.links.items():
            if val == search:
                return key

    def validate(self,URL):
        dotindex = 0
        slashindex = 0
        domain = ""
        domaincheck = ["com", "net", "org", "gov"]
        counter = 0
        for i in URL:
            if i == ".":
                dotindex = URL[counter]
            counter + 1
        #print(dotindex)
        for i in URL:
            counter = 0
            if i == "/":
                slashindex = URL[counter]
            counter + 1
        domain = URL[dotindex:slashindex]
        for i in domaincheck:
            if domain == i:
                return True
        return False

 

state = "0"

url = URLs()

while(state != "00"):
    print("Would you like to: \n   (0) Store a URL\n   (1) Store and return a shortened URL\n   (2) List stored URLs\n   (3) Display number of stored URLs\n   (4) Return a full URL from a shortened input\n")
    state = input()
    if(state == "0"):
        link = input("Please input your link: ")
        if(url.validate(link)):
            url.store(link)
        else:
            print("Invalid link")
    if(state == "1"):
        link = input("Please input your link: ")
        if(url.validate(link)):
            url.store(link)
            url.printShorten(link)
        else:
            print("Invalid link")
    if(state == "2"):
        url.printURLs()
    if(state == "3"):
        print(url.getCount())
    if(state == "4"):
        shortLink = input("Please input a shortened link: ")
        print(url.findShortened(shortLink))

    print("-------------------------------------------------------------------------------------------")
