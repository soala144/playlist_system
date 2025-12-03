from playlist_manager.system import PlaylistSystem
from playlist_manager.playlist import Playlist
from playlist_manager.song import Song
def test_sort():
    s=PlaylistSystem()
    s.playlists={"Z":None,"A":None}
    s.sort_playlists()
    assert list(s.playlists.keys())[0]=="A"

def test_rename_playlist():
    s = PlaylistSystem()
    s.playlists["Old"] = None
    ok = s.rename_playlist("Old", "New")
    assert ok
    assert "New" in s.playlists
    assert "Old" not in s.playlists

def test_delete_playlist():
    s = PlaylistSystem()
    s.playlists["Gone"] = None
    ok = s.delete_playlist("Gone")
    assert ok
    assert "Gone" not in s.playlists

def test_find_duplicates():
    s = PlaylistSystem()
    s.playlists["A"] = Playlist("A")
    s.playlists["B"] = Playlist("B")
    s.playlists["A"].add_song(Song("Dup","X","G"))
    s.playlists["B"].add_song(Song("dup","Y","H"))
    dups = s.find_duplicates()
    assert "dup" in dups
    assert set(dups["dup"]) == {"A","B"}

def test_sort_playlists_order():
    s = PlaylistSystem()
    s.playlists = {"b": None, "A": None, "c": None}
    names = s.sort_playlists()
    assert names == ["A", "b", "c"]
