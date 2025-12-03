from playlist_manager.playlist import Playlist
from playlist_manager.song import Song
from playlist_manager.system import PlaylistSystem
def test_add_song():
    p=Playlist("L")
    p.add_song(Song("A","B","C"))
    assert len(p.songs)==1

def test_add_song_flow():
    s = PlaylistSystem()
    s.add_song("MyList", "X", "Y", "Z")
    assert "MyList" in s.playlists
    assert any(song.name=="X" and song.singer=="Y" and song.genre=="Z" for song in s.playlists["MyList"].songs)

def test_edit_song():
    s = PlaylistSystem()
    s.playlists["L"] = Playlist("L")
    s.playlists["L"].add_song(Song("Old","SingerA","GenreA"))
    ok = s.edit_song("L", "Old", "New", "SingerB", "GenreB")
    assert ok
    song = s.playlists["L"].songs[0]
    assert song.name == "New"
    assert song.singer == "SingerB"
    assert song.genre == "GenreB"

def test_remove_song():
    s = PlaylistSystem()
    s.playlists["L"] = Playlist("L")
    s.playlists["L"].add_song(Song("A","S1","G1"))
    s.playlists["L"].add_song(Song("B","S2","G2"))
    s.remove_song("L", "A")
    assert len(s.playlists["L"].songs) == 1
    assert s.playlists["L"].songs[0].name == "B"
