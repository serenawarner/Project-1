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






state = "0"

while(state != "00"):
    print("Would you like to: \n\nStore a URl (0), \nStore and return a shortened URL (1), \nlist stored URLs (2), \nDisplay number of stored URLs (3), \nReturn a full URl from a shortened input (4) \n\n")
    state = input()
    if(state == "0"):
        break
    if(state == "1"):
        break
    if(state == "2"):
        break
    if(state == "3"):
        break
    if(state == "4"):
        break
    break

