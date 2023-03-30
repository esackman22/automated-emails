import requests
import datetime


class NewsFeed:

    base_url = 'https://newsapi.org/v2/everything?'
    api_key = 'f37d6874ecb045c3a3fee36bd76cdbf1'

    def __init__(self, interest, from_date, to_date, language):
        self.language = language
        self.to_date = to_date
        self.from_date = from_date
        self.interest = interest

    def _build_url(self):

        url = f'{self.base_url}' \
              f'qInTitle={self.interest}&' \
              f'from={self.from_date}&' \
              f'to={self.to_date}&' \
              f'language={self.language}&' \
              f'apiKey={self.api_key}'

        return url

    def _crawl(self):

        url = self._build_url()
        response = requests.get(url)
        content = response.json()
        return content

    def get(self):

        content = self._crawl()
        articles = content['articles'][:20]
        return articles

    def build_email(self):

        articles = self.get()
        email_body = ''
        for article in articles:
            email_body += article['title'] + '\n' + article['url'] + '\n\n'

        return email_body


if __name__ == "__main__":
    today = datetime.date.today().isoformat()
    yesterday = (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
    news_feed = NewsFeed(interest='bitcoin', from_date=yesterday, to_date=today, language='en')
    email = news_feed.build_email()
    print(email)


