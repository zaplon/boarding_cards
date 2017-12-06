class BaseModelMeta(type):
    def __new__(mcls, name, bases, attrs):
        cls = super(BaseModelMeta, mcls).__new__(mcls, name, bases, attrs)
        for attr, obj in attrs.items():
            if isinstance(obj, Field):
                obj.__set_name__(cls, attr)
        return cls


class Field(object):
    required = True
    name = None

    def __init__(self, required=True):
        self.required = required

    def validate(self, val):
        if self.required and not val:
            raise Exception(u"the field is required")

    def __get__(self, obj, objtype):
        return getattr(obj, self.name)

    def __set__(self, obj, val):
        setattr(obj, self.name, self.validate(val))

    # available in python >= 3.6
    def __set_name__(self, owner, name):
        self.name = '_' + name


class CharField(Field):
    def validate(self, val):
        super(CharField, self).validate(val)
        if val is None:
            val = ''
        if type(val) is not str:
            raise Exception(u'value is not string')
        return str(val).lower()


class IntegerField(Field):
    def validate(self, val):
        super(IntegerField, self).validate(val)
        if val is not None:
            return int(val)


class BoardingCard(object, metaclass=BaseModelMeta):
    destination = CharField()
    seat = CharField(required=False)
    gate = IntegerField(required=False)
    departure = CharField()
    extra = CharField(required=False)
    mean_id = CharField()

    def __init__(self, **kwargs):
        for k,v in self.__class__.__dict__.items() :
            if issubclass(v.__class__, Field):
                 setattr(self, k, kwargs.get(k, None))

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
            sentences.append(self.extra.title())
        return '. '.join(sentences)

    def __str__(self):
        data = {'departure': self.departure.title(), 'destination': self.destination.title(), 'mean_id': self.mean_id,
                'details': self.details}
        return "From %(departure)s, %(mean_id)s to %(destination)s%(details)s." % data