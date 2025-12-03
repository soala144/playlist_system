from playlist_manager.system import PlaylistSystem
def test_login_failure(monkeypatch):
    system = PlaylistSystem()
    inputs = iter(["wronguser", "wrongpass", "wrongpass", "wrongpass"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    assert system.login() is False
