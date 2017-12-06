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
    if len(data) == 0:
        return ["No data was provided"]
    cards = []
    for d in data:
        cards.append(BoardingCard(**d))
    number_of_cards = len(cards)
    result = [cards.pop(0)]
    for i in range(0, len(cards)):
        for j in range(0, len(cards)):
            if result[0].departure == cards[j].destination:
                result.insert(0, cards.pop(j))
                break
            elif result[-1].destination == cards[j].departure:
                result += [cards.pop(j)]
                break
    print(result)
    if len(result) != number_of_cards:
        return ["No solution was found"]
    trip_plan = []
    for r in result:
        trip_plan.append(r.__str__())
    return trip_plan
