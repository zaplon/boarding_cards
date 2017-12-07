import json

from boarding_card import BoardingCard


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
    cards = [BoardingCard(**data[0])]
    look_up = {'destinations': {cards[0].destination: 0}, 'departures': {cards[0].departure: 0}}
    result = [0]
    for i in range(1, data_size + 1):
        if i < data_size:
            cards.append(BoardingCard(**data[i]))
            look_up['destinations'][cards[i].destination] = i
            look_up['departures'][cards[i].departure] = i
        elif len(result) == data_size:
            break
        try:
            result.insert(0, look_up['destinations'][cards[result[0]].departure])
            continue
        except KeyError:
            pass
        try:
            result.append(look_up['departures'][cards[result[-1]].destination])
        except KeyError:
            pass
    if len(result) != len(data):
        return ["No solution was found"]
    trip_plan = []
    for r in result:
        trip_plan.append(cards[r].__str__())
    return trip_plan
