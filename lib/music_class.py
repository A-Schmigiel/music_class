"""As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.
"""

class MusicClass():

    def __init__(self):
        self.storage =[]

    def check_track_exists(self, track):
        for index, dictionary in enumerate(self.storage):
            if dictionary['track_name'] == track:
                return index
                
        

    def add(self, author, track):
        index = self.check_track_exists(track)
        if index == None:
            track_info = {'author' : author,
                      'track_name' : track,
                      'times_played' : 1}
            self.storage.append(track_info)
            
        else:
            self.storage[index]["times_played"] += 1


    def list_tracks(self):
        return self.storage
    


#dict structure:
#{author: name
# track: track_name
# times_played: 1}

