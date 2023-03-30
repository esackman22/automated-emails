import yagmail
import creds
import pandas as pd
import numpy as np
import datetime as dt
from news import NewsFeed


people = pd.read_excel('people.xlsx')
today = dt.date.today().isoformat()
yesterday = (dt.date.today() - dt.timedelta(days=1)).isoformat()

for index, row in people.iterrows():

    if row['email'] is np.NAN:
        break

    to_address = row['email']
    interest = row['interest']
    name = row['name']
    news_feed = NewsFeed(interest, yesterday, today, 'en')
    email_body = news_feed.build_email()
    email = yagmail.SMTP(user=creds.email_address, password=creds.password)
    email.send(to=to_address,
               subject=f'Your {interest} news for {today}.',
               contents=f'Hi {name},\nSee what is going on with {interest} today. \n\n{email_body}')


