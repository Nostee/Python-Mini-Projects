import requests
from bs4 import BeautifulSoup
import pprint

hn = []
occupied_rank = []

def sort_stories_by_votes(hn):
        return sorted(hn,key=lambda k:k["points"], reverse=True)

def create_custom_hn(links, subtext,rank):
        for idx, item in enumerate(links):
            title = item.getText()
            ranked = rank[idx].getText()
            href = item.get("href", None)

            vote = subtext[idx].select(".score")
            if len(vote):
                points = int(vote[0].getText().replace(" points", ""))
                properties = {"Rank":ranked,"title": title, "link": href, "points": points}
                
                if(points>=100 and ranked not in occupied_rank):
                    occupied_rank.append(ranked)
                    hn.append(properties)

for page in range(5):
    res = requests.get(f"https://news.ycombinator.com/news?p={page}")
    soup = BeautifulSoup(res.text, "html.parser")
    links = soup.select(".storylink")
    subtext = soup.select(".subtext")
    rank = soup.select(".rank")
    create_custom_hn(links, subtext,rank)

pprint.pprint(hn)
