"""Song entity representing a single track and its metadata."""

class Song:
    """Simple data holder for song name, singer, and genre."""

    def __init__(self, name, singer, genre):
        """Initialize a song with its name, singer, and genre."""
        self.name = name
        self.singer = singer
        self.genre = genre

    def __str__(self):
        """Human-readable representation of the song."""
        return f"{self.name} by {self.singer} ({self.genre})"
