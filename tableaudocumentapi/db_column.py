_ATTRIBUTES = [
    'key',          # Name of the field as specified in the file, usually surrounded by [ ]
    'value'         # Name of the field as referred to in the database
]


class DBColumn(object):
    """ Represents a DB column in a datasource """

    def __init__(self, column_xml=None):

        if column_xml is None:
            raise AttributeError('column_xml needed to initialize field')
        else:
            self._initialize_from_column_xml(column_xml)
            self._xml = column_xml

    def _initialize_from_column_xml(self, xmldata):
        for attrib in _ATTRIBUTES:
            self._apply_attribute(xmldata, attrib, lambda x: xmldata.attrib.get(x, None))

    def _apply_attribute(self, xmldata, attrib, default_func, read_name=None):
        if read_name is None:
            read_name = attrib
        if hasattr(self, '_read_{}'.format(read_name)):
            value = getattr(self, '_read_{}'.format(read_name))(xmldata)
        else:
            value = default_func(attrib)

        setattr(self, '_{}'.format(attrib), value)

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value

    @classmethod
    def from_column_xml(cls, xmldata):
        return cls(column_xml=xmldata)
