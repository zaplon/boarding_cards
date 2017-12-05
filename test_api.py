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
    BoardingCard(departure="Stockholm", destination="Warsaw", seat_number="QW.333", extra='baggage to pick up at exit')


def test_api_properly_process_different_types():
    data = []
    # json returns json
    json.loads(calculate_trip(json.dumps(data)))
    # list return list
    calculate_trip(data) is list


def test_api_returns_proper_results():
    data = [{'departure': 'Warsaw', 'destination': 'Berlin'},
            {'departure': 'Rio', 'destination': 'Paris'},
            {'departure': 'Paris', 'destination': 'Warsaw'},
            {'departure': 'Berlin', 'destination': 'Rio'}
            ]
    calculate_trip(data)
