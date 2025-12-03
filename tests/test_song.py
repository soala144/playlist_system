from playlist_manager.song import Song
def test_song_creation():
    s = Song("Test","Singer","Pop")
    assert s.name=="Test"
