

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

 
