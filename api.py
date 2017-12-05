import json


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
def calculate_trip(cards):
    result = []
    for i in range(0, len(cards)):
        if cards[i].departure == cards[i+1].destination:
            pass
        elif cards[i].destination == cards[i+1].departure:
            pass
    return result
