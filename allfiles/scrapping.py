import requests
from bs4 import BeautifulSoup

def scrape(topic_name):

    for i in range(1):
        l = []
        
        for i in topic_name:
            #getting all html data from the website with particular topic
            req = requests.get(f"https://www.news18.com/topics/{i}/")
            soup = BeautifulSoup(req.content, "html.parser")

            #finds only headlines from all the data and adds them to a list
            filtered = soup.find_all('p',attrs = {"class":"jsx-4247059639"})
            filtered = list(filtered)
            for i in filtered:
                l += i
            
        if l == []:
                return(['No updates from the topics you follow'])
        return l

    #except:
    print("Wasn't able to scrape data")

