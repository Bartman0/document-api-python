from tableaudocumentapi import Clause

class Relation(object):
    """A class representing parameters inside Data Sources."""

    def __init__(self, relation_xml):
        """Relation is usually instantiated by passing in relation XML
        from a Connection.
        """
        self._relationXML = relation_xml
        self._type = relation_xml.get('type')
        self._join = relation_xml.get('join')
        self._name = relation_xml.get('name')
        self._table = relation_xml.get('table')
        self._connection = relation_xml.get('connection')

        self._clause = list(map(Clause, self._relationXML.findall('./clause')))
        self._relations = list(map(Relation, self._relationXML.findall('./relation')))

    @property
    def type(self):
        return self._type

    @property
    def join(self):
        return self._join

    @property
    def name(self):
        return self._name

    @property
    def table(self):
        return self._table

    @property
    def connection(self):
        return self._connection

    def __str__(self):
        if self.type == "table":
            return f'{self.table} "{self.name}"'
        if self.type == "join":
            return f"{self._relations[0]} {self.join} {self.type} {self._relations[1]} on ({self._clause[0]})"
        return "ERROR"
