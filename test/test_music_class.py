from lib.music_class import MusicClass

def test_class_has_a_storage():
    tunes = MusicClass()

    assert isinstance(tunes.storage, list)


def test_adds_new_item_to_the_list():
    tunes = MusicClass()
    tunes.add("Du Hast")

    assert tunes.storage == ["Du Hast"]

def test_returns_list():
    tunes = MusicClass()
    tunes.add("Du Hast")
    result = tunes.list_tracks()

    assert isinstance(result, list)

def test_list_returns_list_of_tracks_added():
    tunes = MusicClass()
    tunes.add("Du Hast")
    tunes.add("All that jazz")
    result = tunes.list_tracks()

    assert result == ["Du Hast", "All that jazz"]