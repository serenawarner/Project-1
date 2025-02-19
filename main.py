class URLs:
    def __init__(self):
        self.links = {}
        self.count = 0
        return

    def shorten(self,URL):
        url =  "www.myLink.com/" + str(self.count)
        self.count+=1
        return url

    def store(self,URL):
        self.links[URL] = self.shorten(URL)

    def printShorten(self,URL):
        print(self.links[URL])



