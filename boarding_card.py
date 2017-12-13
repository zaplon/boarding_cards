class BoardingCard(object):

    def __init__(self, **kwargs):
        self.destination = kwargs['destination']
        self.departure = kwargs['departure']
        if not (type(self.destination) is str and type(self.departure) is str):
            raise Exception("Departure and destination should be strings")
        self.mean_id = kwargs.get('mean_id')  # for example bus number, flight number
        self.extra = kwargs.get('extra', None)  # non-obligatory additional info like baggage transfer
        self.seat = kwargs.get('seat', None)  # non-obligatory
        self.gate = kwargs.get('gate', None)  # non-obligatory gate number

    # for nice display in python console
    def __repr__(self):
        return '%s -> %s' % (self.departure, self.destination)

    @property
    def details(self):
        parts = []
        sentences = ['']
        if self.gate:
            parts.append('go to gate %s' % self.gate)
        if self.seat:
            parts.append('seat %s' % self.seat)
        text = ', '.join(parts)
        if len(parts) > 0:
            text = text[0].upper() + text[1:]
            sentences.append(text)
        if self.extra:
            sentences.append(self.extra[0].upper() + self.extra[1:])
        return '. '.join(sentences)

    # human-readable instructions
    def __str__(self):
        data = {'departure': self.departure.title(), 'destination': self.destination.title(), 'mean_id': self.mean_id,
                'details': self.details}
        return "From %(departure)s, %(mean_id)s to %(destination)s%(details)s." % data
