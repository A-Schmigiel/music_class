from lib.music_class import MusicClass

def test_class_has_a_storage():
    tunes = MusicClass()

    assert isinstance(tunes.storage, list)


def test_adds_new_item_to_the_list():
    tunes = MusicClass()
    tunes.add("Rammstein", "Du Hast")
    tunes.add("Rammstein", "Du Hast")
    tunes.add("Chicago_musical", "All that jazz")

    assert tunes.storage == [{"author": "Rammstein",
                              "track_name": "Du Hast",
                              "times_played": 2},
                              {"author": "Chicago_musical",
                              "track_name": "All that jazz",
                              "times_played": 1}]

def test_returns_list():
    tunes = MusicClass()
    tunes.add("Rammstein", "Du Hast")
    result = tunes.list_tracks()

    assert isinstance(result, list)

def test_list_returns_list_of_tracks_added():
    tunes = MusicClass()
    tunes.add("Rammstein", "Du Hast")
    tunes.add("Chicago_musical", "All that jazz")
    result = tunes.list_tracks()

    assert result == [{"author": "Rammstein",
                              "track_name": "Du Hast",
                              "times_played": 1},
                              {"author": "Chicago_musical",
                              "track_name": "All that jazz",
                              "times_played": 1}]