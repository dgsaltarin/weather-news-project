from ..models.news import News

class MapNews():
    def mapObjectToNews(obj):
        news: list[News] = []
        for articleIndex in range(len(obj)):
            article = obj[articleIndex]
            news_article: News = News(title=article['title'], author=article['author'], summary=article['summary'], link=article['link'], media=article['media'])
            news.append(news_article)
        return news    