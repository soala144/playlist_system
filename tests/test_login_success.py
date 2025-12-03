from playlist_manager.system import PlaylistSystem
def test_login(monkeypatch):
    system = PlaylistSystem()
    inputs = iter(["user123", "Givemetheykey123"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    assert system.login() is True
