from playlist_manager.system import PlaylistSystem

def test_import(tmp_path):
    system = PlaylistSystem()

    file_path = tmp_path / "songs.txt"
    file_path.write_text("SongA,SingerA,Pop\nSongB,SingerB,Rock\n")

    count = system.import_playlist("ImportedList", file_path)
    assert count == 2
    songs = [s.name for s in system.playlists["ImportedList"].songs]
    assert "SongA" in songs
    assert "SongB" in songs
