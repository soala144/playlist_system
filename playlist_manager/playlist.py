"""Playlist module that manages collections of songs and operations on them."""

import random
from .song import Song

class Playlist:
    """A named collection of `Song` objects with utility operations."""

    def __init__(self, name):
        """Create a playlist with a given `name` and an empty song list."""
        self.name = name
        self.songs = []

    def add_song(self, song):
        """Append a `Song` to this playlist."""
        self.songs.append(song)

    def remove_song(self, song_name):
        """Remove all songs whose name matches `song_name` (case-insensitive)."""
        # Filter out any songs whose lowercase name equals the target name
        self.songs = [s for s in self.songs if s.name.lower() != song_name.lower()]

    def update_song(self, old, new, singer, genre):
        """Update the first song matching `old` with new metadata; return True if changed."""
        for s in self.songs:
            if s.name.lower() == old.lower():
                s.name = new
                s.singer = singer
                s.genre = genre
                return True
        return False

    def sort_songs(self):
        """Sort songs in-place by name, case-insensitive."""
        self.songs.sort(key=lambda s: s.name.lower())

    def shuffle_songs(self):
        """Shuffle songs in-place using random order."""
        random.shuffle(self.songs)

    def has_duplicate(self, name):
        """Return True if more than one song matches `name` (case-insensitive)."""
        # Count songs with matching lowercase name and check if count exceeds 1
        return sum(1 for s in self.songs if s.name.lower() == name.lower()) > 1
