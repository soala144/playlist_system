import time
from playlist_manager.playlist import Playlist
from playlist_manager.song import Song

class PlaylistSystem:
    """Interactive playlist manager with authentication and playlist operations.

    Provides flows and helpers to add/edit/remove songs, manage playlists,
    detect duplicates, sort/shuffle, and export/import playlists.
    """
    def __init__(self):
        self.playlists = {}
        self.username = "user123"
        self.password = "Givemetheykey123"

    def login(self):
        """Authenticate the user before granting access to features.

        Prompts for username once; if recognized, allows up to three
        password attempts. On incorrect password, prints an error and
        re-prompts for password without asking for username again.

        Returns True on success; otherwise returns False after exhausting
        attempts or when username is unrecognized.
        """
        attempts = 3
        user = input("Username: ")
        if user != self.username:
            print("Username not recognized.")
            return False
        while attempts > 0:
            pw = input("Password: ")
            if pw == self.password:
                print("Login successful")
                return True
            attempts -= 1
            if attempts > 0:
                print("Password is not correct")
        print("Too many attempts. Locked (simulated).")
        return False

    def run(self):
        # Main event loop; shows menu and dispatches choices after login.
        if not self.login():
            return
        while True:
            print("""
1. Add song
2. Edit song
3. Rename playlist
4. Delete playlist
5. Remove song
6. Find duplicates
7. Sort playlists
8. Sort songs
9. Shuffle songs
10. Export
11. Exit
12. Import playlist from file
""")
            self.handle_menu(input("Choose: "))

    def handle_menu(self, c):
        # Dispatch menu option to the corresponding flow using a dictionary.
        match c:
            case "1":
                self.add_song_flow()
            case "2":
                self.edit_song_flow()
            case "3":
                self.rename_playlist_flow()
            case "4":
                self.delete_playlist_flow()
            case "5":
                self.remove_song_flow()
            case "6":
                self.find_duplicates_flow()
            case "7":
                self.sort_playlists()
            case "8":
                self.sort_songs_in_playlists()
            case "9":
                self.shuffle_songs_in_playlists()
            case "10":
                self.export_playlists()
            case "11":
                exit()
            case "12":
                self.import_playlist_flow()
            case _:
                print("Invalid")

    # Empty placeholder flows
    def add_song_flow(self):
        # Collect song details and add to the given playlist.
        playlist_name = input("Playlist name: ")
        name = input("Song name: ")
        singer = input("Singer: ")
        genre = input("Genre: ")
        self.add_song(playlist_name, name, singer, genre)
        print("Song added successfully.")

    def edit_song_flow(self):
        # Edit an existing song's name/singer/genre inside a playlist.
        playlist_name = input("Playlist name: ")
        if playlist_name not in self.playlists:
            print("Playlist not found.")
            return
        old = input("Old song name: ")
        new = input("New song name: ")
        singer = input("New singer: ")
        genre = input("New genre: ")
        updated = self.playlists[playlist_name].update_song(old, new, singer, genre)
        if updated:
            print("Song updated.")
        else:
            print("Song not found.")
    def rename_playlist_flow(self):
        # Rename a playlist if the old exists and new does not.
        old_name = input("Current playlist name: ")
        new_name = input("New playlist name: ")
        if old_name not in self.playlists:
            print("Playlist not found.")
            return
        if new_name in self.playlists:
            print("A playlist with this name already exists.")
            return
        self.playlists[new_name] = self.playlists.pop(old_name)
        print("Playlist renamed.")
    def delete_playlist_flow(self):
        # Delete a playlist by name if it exists.
        name = input("Playlist name: ")
        if name in self.playlists:
            del self.playlists[name]
            print("Playlist deleted.")
        else:
            print("Playlist not found.")
    def remove_song_flow(self):
        """Remove a song by name from the specified playlist."""
        playlist_name = input("Playlist name: ")
        if playlist_name not in self.playlists:
            print("Playlist not found.")
            return
        song_name = input("Song name to remove: ")
        self.playlists[playlist_name].remove_song(song_name)
        print("Song removed.")
    def find_duplicates_flow(self):
        """Scan playlists and print duplicate songs across or within lists."""
        duplicates = self.find_duplicates()
        if duplicates:
            for name, lists in duplicates.items():
                print(f"Duplicate song found: {name} in playlists: {', '.join(lists)}")
        else:
            print("No duplicates found.")

    def import_playlist_flow(self):
        """Import songs from a file into a named playlist."""
        playlist_name = input("Playlist name: ")
        path = input("File path: ")
        count = self.import_playlist(playlist_name, path)
        if count > 0:
            print("Playlist imported.")
        else:
            print("No songs imported.")

    def add_song(self, playlist_name, name, singer, genre):
        """Add a song to a playlist, creating the playlist if missing."""
        if playlist_name not in self.playlists:
            self.playlists[playlist_name] = Playlist(playlist_name)
        song = Song(name, singer, genre)
        self.playlists[playlist_name].add_song(song)

    def edit_song(self, playlist_name, old, new, singer, genre):
        """Edit a song in a playlist; returns True if updated, else False."""
        if playlist_name not in self.playlists:
            return False
        return self.playlists[playlist_name].update_song(old, new, singer, genre)

    def sort_playlists(self):
        """Sort playlists case-insensitively and return the ordered names."""
        # Use stable sort with case-insensitive key for predictable ordering
        sorted_items = sorted(self.playlists.items(), key=lambda x: x[0].lower())
        self.playlists = dict(sorted_items)
        print("Playlists sorted")
        return [name for name, _ in sorted_items]

    def sort_songs_in_playlists(self):
        """Sort songs in each playlist and return mapping of names -> orders."""
        result = {}
        for name, p in self.playlists.items():
            p.sort_songs()
            result[name] = [s.name for s in p.songs]
        print("Songs sorted")
        return result

    def shuffle_songs_in_playlists(self):
        """Shuffle songs in each playlist and return mapping of names -> orders."""
        result = {}
        for name, p in self.playlists.items():
            p.shuffle_songs()
            result[name] = [s.name for s in p.songs]
        print("Songs shuffled")
        return result

    def export_playlists(self):
        """Export all playlists to the default exports file and print status."""
        self.export_to_file("exports/exported_playlists.txt")
        print("Exported")
    
    def rename_playlist(self, old_name, new_name):
        """Rename a playlist; returns True on success, False otherwise."""
        if old_name not in self.playlists:
            return False
        if new_name in self.playlists:
            return False
        self.playlists[new_name] = self.playlists.pop(old_name)
        return True

    def delete_playlist(self, name):
        # Delete a playlist by name; returns True if deleted, else False.
        if name in self.playlists:
            del self.playlists[name]
            return True
        return False

    def remove_song(self, playlist_name, song_name):
        # Remove a song from a playlist; returns True if playlist exists.
        if playlist_name not in self.playlists:
            return False
        self.playlists[playlist_name].remove_song(song_name)
        return True

    def find_duplicates(self):
        """Return duplicates across playlists or multiple in one.

        The return value maps lowercase song names to the list of playlist
        names in which they occur at least once, when either:
        - The song appears in more than one playlist, or
        - It appears multiple times within any single playlist.
        """
        occ = {}

        for pname, playlist in self.playlists.items():
            counts = {}
            for s in playlist.songs:
                key = s.name.lower()
                counts[key] = counts.get(key, 0) + 1
            for key, cnt in counts.items():
                if key not in occ:
                    occ[key] = {}
                occ[key][pname] = cnt
        result = {}

        for key, per_pl in occ.items():
            pl_names = list(per_pl.keys())
            multiple_playlists = len(pl_names) > 1
            any_duplicates_in_one = any(cnt > 1 for cnt in per_pl.values())
            if multiple_playlists or any_duplicates_in_one:
                result[key] = pl_names
        return result

    def get_sorted_playlist_names(self):
        """Convenience wrapper to sort playlists and return their names."""
        return self.sort_playlists()

    def get_sorted_song_names(self, playlist_name):
        """Sort a playlist's songs and return the ordered list of names."""
        if playlist_name not in self.playlists:
            return []
        p = self.playlists[playlist_name]
        p.sort_songs()
        return [s.name for s in p.songs]

    def get_shuffled_song_names(self, playlist_name):
        """Shuffle a playlist's songs and return the current list of names."""
        if playlist_name not in self.playlists:
            return []
        p = self.playlists[playlist_name]
        p.shuffle_songs()
        return [s.name for s in p.songs]

    def export_to_file(self, path):
        """Write all playlists and songs to a file at "path"."""
        with open(path, "w") as f:
            for name, p in self.playlists.items():
                f.write(f"Playlist: {name}\n")
                for s in p.songs:
                    f.write(f"- {s.name} by {s.singer} ({s.genre})\n")

    def import_playlist(self, playlist_name, path):
        """Import songs from a comma-separated file into a playlist.

        Each non-empty line must be of the form "Name,Artist,Genre".
        Returns the number of songs imported; creates the playlist if
        it does not already exist. Invalid lines are skipped.
        """
        if playlist_name not in self.playlists:
            self.playlists[playlist_name] = Playlist(playlist_name)
        count = 0

        try:
            with open(path, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = [p.strip() for p in line.split(",")]
                    if len(parts) != 3:
                        continue
                    name, singer, genre = parts
                    self.playlists[playlist_name].add_song(Song(name, singer, genre))
                    count += 1
                    
        except FileNotFoundError:
            return 0
        
        return count
