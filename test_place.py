"""(Incomplete) Tests for Place class."""
from place import Place

def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visit

    # Test initial-value place

    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    print(new_place)
    assert new_place.is_visit

    new_place.unvisit()
    print(new_place)
    assert not new_place.is_visit

    # TODO: Write tests to show this initialisation works


    # TODO: Add more tests, as appropriate, for each method

if __name__ == '__main__':
    run_tests()