from exceptions import Exception


class Field(object):
    required = True
    value = None

    def validate(self):
        if self.required and not self.value:
            raise Exception(u"the field is required")


class BoardingCard(object):
    destination = CharField()
    seat_number = IntegerField()
    departure = CharField()
    id_number = CharFIeld()