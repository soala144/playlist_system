import time
from playlist_manager.playlist import Playlist
from playlist_manager.song import Song

class PlaylistSystem:
    def __init__(self):
        self.playlists = {}
        self.username = "user123"
        self.password = "Givemetheykey123"

    def login(self):
        attempts = 3
        while attempts > 0:
            user = input("Username: ")
            pw = input("Password: ")
            if user == self.username and pw == self.password:
                print("Login successful")
                return True
            attempts -= 1
        print("Too many attempts. Locked (simulated).")
        return False

    def run(self):
        if not self.login():
            return
        while True:
            print("""
1 Add song
2 Edit song
3 Rename playlist
4 Delete playlist
5 Remove song
6 Find duplicates
7 Sort playlists
8 Sort songs
9 Shuffle songs
10 Export
11 Exit
""")
            self.handle_menu(input("Choose: "))

    def handle_menu(self, c):
        if c=="1": self.add_song_flow()
        elif c=="2": self.edit_song_flow()
        elif c=="3": self.rename_playlist_flow()
        elif c=="4": self.delete_playlist_flow()
        elif c=="5": self.remove_song_flow()
        elif c=="6": self.find_duplicates_flow()
        elif c=="7": self.sort_playlists()
        elif c=="8": self.sort_songs_in_playlists()
        elif c=="9": self.shuffle_songs_in_playlists()
        elif c=="10": self.export_playlists()
        elif c=="11": exit()
        else: print("Invalid")

    # Empty placeholder flows
    def add_song_flow(self):
        playlist_name = input("Playlist name: ")
        name = input("Song name: ")
        singer = input("Singer: ")
        genre = input("Genre: ")
        self.add_song(playlist_name, name, singer, genre)
        print("Song added successfully.")
    def edit_song_flow(self):
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
        name = input("Playlist name: ")
        if name in self.playlists:
            del self.playlists[name]
            print("Playlist deleted.")
        else:
            print("Playlist not found.")
    def remove_song_flow(self):
        playlist_name = input("Playlist name: ")
        if playlist_name not in self.playlists:
            print("Playlist not found.")
            return
        song_name = input("Song name to remove: ")
        self.playlists[playlist_name].remove_song(song_name)
        print("Song removed.")
    def find_duplicates_flow(self):
        duplicates = self.find_duplicates()
        if duplicates:
            for name, lists in duplicates.items():
                print(f"Duplicate song found: {name} in playlists: {', '.join(lists)}")
        else:
            print("No duplicates found.")

    def add_song(self, playlist_name, name, singer, genre):
        if playlist_name not in self.playlists:
            self.playlists[playlist_name] = Playlist(playlist_name)
        song = Song(name, singer, genre)
        self.playlists[playlist_name].add_song(song)

    def edit_song(self, playlist_name, old, new, singer, genre):
        if playlist_name not in self.playlists:
            return False
        return self.playlists[playlist_name].update_song(old, new, singer, genre)

    def sort_playlists(self):
        sorted_items = sorted(self.playlists.items(), key=lambda x: x[0].lower())
        self.playlists = dict(sorted_items)
        print("Playlists sorted")
        return [name for name, _ in sorted_items]

    def sort_songs_in_playlists(self):
        for p in self.playlists.values(): p.sort_songs()
        print("Songs sorted")

    def shuffle_songs_in_playlists(self):
        for p in self.playlists.values(): p.shuffle_songs()
        print("Songs shuffled")

    def export_playlists(self):
        with open("exports/exported_playlists.txt","w") as f:
            for name, p in self.playlists.items():
                f.write(name + " -> " + ", ".join([s.name for s in p.songs]) + "\n")
        print("Exported")
    
    def rename_playlist(self, old_name, new_name):
        if old_name not in self.playlists:
            return False
        if new_name in self.playlists:
            return False
        self.playlists[new_name] = self.playlists.pop(old_name)
        return True

    def delete_playlist(self, name):
        if name in self.playlists:
            del self.playlists[name]
            return True
        return False

    def remove_song(self, playlist_name, song_name):
        if playlist_name not in self.playlists:
            return False
        self.playlists[playlist_name].remove_song(song_name)
        return True

    def find_duplicates(self):
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
        return self.sort_playlists()
