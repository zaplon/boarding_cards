class Field(object):
    required = True
    value = None

    def __init__(self, required=True):
        self.required = required

    def validate(self, val):
        if self.required and not val:
            raise Exception(u"the field is required")

    def __get__(self, obj):
        return self.value

    def __set__(self, obj, val):
        self.validate(val)


class CharField(Field):
    def validate(self, val):
        super(CharField, self).validate(val)
        if type(val) not in [str, unicode]:
            raise Exception(u'value is not string')
        self.value = str(val)


class IntegerField(Field):
    def validate(self, val):
        super(IntegerField, self).validate(val)
        self.value = int(val)


class BoardingCard(object):
    destination = CharField()
    seat_number = CharField(required=False)
    departure = CharField()
    extra = CharField(required=False)

    def __init__(self, **kwargs):
        for k,v in BoardingCard.__dict__.items() :
            if issubclass(v.__class__, Field):
                setattr(self, k, kwargs.get(k, None))
