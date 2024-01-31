from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)
movie_webpage = response.text
movie_titles = []

soup = BeautifulSoup(movie_webpage, "html.parser")
titles = soup.find_all(name="h3", class_="title")
for title in titles:
    movie_titles.append(title.text)

reverse_list = list(reversed(movie_titles))

#save movies as txt file 
with open("movies.txt", "w", encoding='utf-8') as f:
    for movies in reverse_list:
        f.write(f'{movies}\n')
print("File written successfully")
    