from bs4 import BeautifulSoup
import requests



class Billboard:

    def __init__(self):
        self.date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    
    def date(self):
        return self.date
        
    
    def song_names(self):
        self.response = requests.get(f"https://www.billboard.com/charts/hot-100/{self.date}")
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.song_names_spans = self.soup.select("li ul li h3")
        self.song_names = [song.getText().strip() for song in self.song_names_spans]
        song_list = self.song_names

        return song_list