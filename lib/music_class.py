class MusicClass():
    def __init__(self):
        self.storage = []

    def add(self, track):
        self.storage.append(track)

    def list_tracks(self):
        return self.storage