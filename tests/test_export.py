from playlist_manager.system import PlaylistSystem
def test_export(tmp_path):
    
    system = PlaylistSystem()
    system.add_song("MyList", "Song1", "Singer1", "Pop")
    system.add_song("MyList", "Song2", "Singer2", "Rock")

    file_path = tmp_path / "export.txt"
    system.export_to_file(file_path)

    content = file_path.read_text()
    assert "Song1 by Singer1" in content
    assert "Song2 by Singer2" in content
    assert "Playlist: MyList" in content
