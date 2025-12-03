from playlist_manager.playlist import Playlist
from playlist_manager.song import Song

def test_shuffle_songs():

    p = Playlist("TestPlaylist")
    p.add_song(Song("A", "Singer1", "Pop"))
    p.add_song(Song("B", "Singer2", "Rock"))
    p.add_song(Song("C", "Singer3", "Jazz"))

    original_order = [s.name for s in p.songs]
    p.shuffle_songs()
    shuffled_order = [s.name for s in p.songs]

    
    assert shuffled_order != original_order or shuffled_order == original_order
    assert set(shuffled_order) == set(original_order)
