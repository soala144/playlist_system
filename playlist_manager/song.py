class Song:
    def __init__(self, name, singer, genre):
        self.name = name
        self.singer = singer
        self.genre = genre
    def __str__(self):
        return f"{self.name} by {self.singer} ({self.genre})"
