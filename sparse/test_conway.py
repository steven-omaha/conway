import pytest

from conway import _get_neighbours, iterate, _get_alive_neighbour_count
import objects


def test_blinker():
    assert iterate(objects.blinker_horizontal) == objects.blinker_vertical
    assert iterate(objects.blinker_vertical) == objects.blinker_horizontal


def test_block():
    assert iterate(objects.block) == objects.block


def test_glider():
    field = objects.glider
    result = field.copy()
    for i in range(4):
        result = iterate(result)
    assert result == {(x + 1, y - 1) for x, y in field}


def test__get_neighbours():
    neighbours = _get_neighbours((1, 1))
    assert neighbours == {
        (0, 0),
        (1, 0),
        (2, 0),
        (2, 1),
        (2, 2),
        (1, 2),
        (0, 2),
        (0, 1),
    }


@pytest.mark.parametrize("cell, field, result, description", [
    [
        (1, 1),
        {
            (0, 0),
            (1, 0),
            (2, 0),
            (2, 1),
            (2, 2),
            (1, 2),
            (0, 2),
            (0, 1),
        },
        8,
        "8 neighbours"
    ],
    [
        (0, 0),
        set(),
        0,
        "0 neighbours"
    ],
    [
        (9, 9),
        {
            (9, 8),
        },
        1,
        "1 neighbour"
    ],
    [
        (7, 5),
        {
            (7, 4),
            (6, 5),
        },
        2,
        "2 neighbours"
    ],
])
def test__get_alive_neighbour_count(cell, field, result, description):
    # noinspection PyTypeChecker
    assert (_get_alive_neighbour_count(cell, field) == result), description
