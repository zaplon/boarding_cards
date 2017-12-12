import json
from collections import deque

from boarding_card import BoardingCard


# decorator that ensures proper input and output formats
def api_view(func):
    def wrapper(data):
        parsers = [(list, list), (json.loads, json.dumps)]
        serializer = None
        for parser in parsers:
            try:
                parsed_data = parser[0](data)
                serializer = parser[1]
            except:
                continue
        if serializer:
            return serializer(func(parsed_data))
        else:
            raise Exception('Data could not be decoded!')
    return wrapper


@api_view
def calculate_trip(data):

    if type(data) is not list:
        raise Exception("List should be provided")
    data_size = len(data)
    if data_size == 0:
        return ["No data was provided"]

    def add_card(cards, look_up):
        try:
            # check if card fits at the begging
            result.appendleft(look_up['destinations'][cards[result[0]].departure])
        except KeyError:
            try:
                # so maybe it fits at the end?
                result.append(look_up['departures'][cards[result[-1]].destination])
            except KeyError:
                pass

    # initialization
    # deque is faster in appending at both ends than list
    result = deque([0], maxlen=data_size)
    cards = []
    look_up = {'destinations': {}, 'departures': {}}

    for i, card in enumerate(data):
        cards.append(BoardingCard(**card))
        look_up['destinations'][cards[i].destination] = i
        look_up['departures'][cards[i].departure] = i
        add_card(cards, look_up)
    add_card(cards, look_up)

    if len(result) != len(data):
        return ["No solution was found"]
    trip_plan = []
    for r in result:
        trip_plan.append(cards[r].__str__())
    return trip_plan
