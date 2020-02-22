from tableaudocumentapi import Expression

class Clause(object):
    """A class representing clauses inside Relations."""

    def __init__(self, clause_xml):
        """Clause is usually instantiated by passing in relation XML
        from a Connection.
        """
        self._clauseXML = clause_xml
        self._type = clause_xml.get('type')
        self._expressions = list(map(Expression, self._clauseXML.findall('./expression')))

    @property
    def type(self):
        return self._type

    @property
    def expression(self):
        return self._expression

    def __str__(self):
        if self.type == "join":
            return f"{self._expressions[0]}"
        return "ERROR"