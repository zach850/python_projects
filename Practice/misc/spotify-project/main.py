from bs4 import BeautifulSoup
import requests

# ask user what year of music to search for
# get_ymd_format = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
get_ymd_format = "1998-06-08"
music_list = []

response = requests.get(f"https://www.billboard.com/charts/hot-100/{get_ymd_format}/")
billboard = response.text

soup = BeautifulSoup(billboard, "html.parser")

song_names_span = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_span]
print(song_names)



