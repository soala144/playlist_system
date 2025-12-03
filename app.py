"""Entry point module for launching the PlaylistSystem CLI application."""

from playlist_manager.system import PlaylistSystem

def main():
    """Instantiate and run the interactive playlist system."""
    system = PlaylistSystem()
    system.run()

if __name__ == "__main__":
    main()
