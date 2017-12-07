from boarding_card import BoardingCard
from api import calculate_trip
import pytest
import json


def test_boarding_card_validation():
    # not enough parameters
    with pytest.raises(Exception):
        BoardingCard(departure="London")

    # wrong type of parameter
    with pytest.raises(Exception):
        BoardingCard(departure="Moscow", destination=1, seat_number='AZ/123')

    # proper initialization
    BoardingCard(departure="Stockholm", destination="Warsaw", seat_number="QW.333", extra='baggage to pick up at exit',
                 mean_id='flight opq/367')


def test_api_properly_process_different_types():
    data = []
    # json returns json
    json.loads(calculate_trip(json.dumps(data)))
    # list return list
    calculate_trip(data) is list


def test_api_returns_proper_results():
    data = [{'departure': 'Warsaw', 'destination': 'Berlin', 'mean_id': 'bus nr 102'},
            {'departure': 'Rio', 'destination': 'New York', 'mean_id': 'baloon',
             'extra': 'baggage will be waiting on the destination point'},
            {'departure': 'Paris', 'destination': 'Warsaw', 'mean_id': 'flight owe/332',
             'gate': 22},
            {'departure': 'Berlin', 'destination': 'Rio', 'mean_id': 'flight azzz.733',
             'seat': 'B45', 'gate': 11}
            ]
    res = calculate_trip(data)
    assert len(res) == 4
    assert res[0].startswith('From Paris')

    data = []
    res = calculate_trip(data)
    assert len(res) == 1

    data = [{'departure': 'Barcelona', 'destination': 'Madrid', 'mean_id': 'bus nr 1'},
            {'departure': 'Baku', 'destination': 'London', 'mean_id': 'flight 23115432'}]
    res = calculate_trip(data)
    assert res == ["No solution was found"]

    data = [{'departure': 'Barcelona', 'destination': 'Madrid', 'mean_id': 'bus nr 1'},
            {'departure': 'Madrid', 'destination': 'Barcelona', 'mean_id': 'bus nr 1'},
            {'departure': 'Barcelona', 'destination': 'Madrid', 'mean_id': 'bus nr 1'}]
    res = calculate_trip(data)
    assert len(res) == 3

    data = [{'departure': 'Barcelona', 'destination': 'Barcelona', 'mean_id': 'bus nr 1'}]
    res = calculate_trip(data)
    assert len(res) == 1