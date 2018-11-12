# pip install newsapi-python

# importing from the NewsAPI
from newsapi import NewsApiClient

# need authorization to use the API
api = NewsApiClient(api_key="6a4868e524a443f9a9a205a10c7e981e")
top_headlines = api.get_top_headlines(sources='daily-mail')

articles = top_headlines["articles"]

print("# articles: " + str(len(articles)))
i = 1
for article in articles:
    print("article #" + str(i) + "\n--------------------")

    #source = article["source"]["name"]
    #print(source)
    title = article["title"]
    content = article["content"]
    #print("\tsource:" + str(source))
    print("\ttitle:" + title)
    print("\tcontent:" + str(content) + "\n")

    i += 1

#api.get_top_headlines(sources="names of sources (ex. ABC News, BBC News")

# accesing from the /v2/top-headlines endpoint
#top_headlines = api.get_top_headlines(q='trump', sources='bbc-news', category='business')

# accessing from the /v2/everything endpoint
#all_articles = api.get_everything(q='trump', sources='BBC News')
# accessing from the /v2/sources endpoint
#news_sources = api.get_sources()
#print(news_sources)
