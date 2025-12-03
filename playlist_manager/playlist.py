import random
from .song import Song

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_name):
        self.songs = [s for s in self.songs if s.name.lower() != song_name.lower()]

    def update_song(self, old, new, singer, genre):
        for s in self.songs:
            if s.name.lower() == old.lower():
                s.name = new
                s.singer = singer
                s.genre = genre
                return True
        return False

    def sort_songs(self):
        self.songs.sort(key=lambda s: s.name.lower())

    def shuffle_songs(self):
        random.shuffle(self.songs)

    def has_duplicate(self, name):
        return sum(1 for s in self.songs if s.name.lower() == name.lower()) > 1
