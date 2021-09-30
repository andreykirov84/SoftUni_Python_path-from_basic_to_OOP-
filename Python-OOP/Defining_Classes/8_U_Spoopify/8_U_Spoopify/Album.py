class Album
    def __init__(self, name, songs):
        self.name = name
        self.songs = []
        self.songs = songs
        self.published = False

    def add_song(self, song: Song):