import yagmail
import pandas
from news import NewsFeed

df = pandas.read_excel('people.xlsx')

for index, row in df.iterrows():
    news_feed = NewsFeed(interest=row["interest"], from_date='2025-09-29', to_date='2025-09-30')
    email = yagmail.SMTP(user='pythoncourse1@gmail.com', password="python_pro_course_1")
    email.send(to=row['email'],
               subject=f'Your {row['interest']}  news for today!',
               contents=f"Hi {row["name"]}\n See what's on about {row["interest"]} Today. \n{news_feed.get()}\nDinesh",)

