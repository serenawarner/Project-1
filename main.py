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

    def validate(URL):
        return True

state = "0"

url = URLs()

while(state != "00"):
    print("Would you like to: \n\nStore a URl (0), \nStore and return a shortened URL (1), \nlist stored URLs (2), \nDisplay number of stored URLs (3), \nReturn a full URL from a shortened input (4) \n\n")
    state = input()
    if(state == "0"):
        link = input("Please input your link: ")
        url.store(link)
    if(state == "1"):
        link = input("Please input your link: ")
        url.store(link)
        url.printShorten(link)
    if(state == "2"):
        url.printURLs()
    if(state == "3"):
        print(url.getCount())
    if(state == "4"):
        url.findShortened("https://www.myLink.com/short0")

 
