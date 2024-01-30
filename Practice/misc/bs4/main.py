from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find("a").get("href")
    article_links.append(link)

article_upvotes = [
    int(score.getText().split()[0])
    for score in soup.find_all(name="span", class_="score")
]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

highest_number = max(article_upvotes)
index_highest_number = article_upvotes.index(highest_number)

print(article_texts[index_highest_number])
print(article_links[index_highest_number])
print(article_upvotes[index_highest_number])


# html_file = "website.html"

# try:
#     with open(html_file, "r", encoding="utf-8") as file:
#         contents = file.read()
# except FileNotFoundError:
#     print(f"File '{html_file}' not found.")
# except UnicodeDecodeError as e:
#     print(f"Error decoding file '{html_file}': {e}")
# except Exception as e:
#     print(f"An error occurred: {e}")

# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())

# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get('href'))
#     pass

# h1_tag = soup.find(name='h1', id="name")
# # print(h1_tag.string)

# section_heading = soup.find(name='h3', class_='heading')
# # print(section_heading.string)

# #use css selector
# company_url = soup.select_one(selector="p a")
# # print(company_url)

# headings = soup.select(".heading")
# print(headings)
