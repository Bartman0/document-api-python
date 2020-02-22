class Expression(object):
    """A class representing expression inside Data Sources."""

    _LOGICALS = [
        'AND',
        'OR'
    ]

    _COMPARISONS = [
        '=',
        '>',
        '>=',
        '<',
        '<=',
        '!=',
        '<>'
    ]

    _OPS = _LOGICALS + _COMPARISONS

    def __init__(self, expression_xml):
        """Expression is usually instantiated by passing in expression XML
        from a Relation.
        """
        self._expressionXML = expression_xml
        self._op = expression_xml.get('op')
        self._expressions = list(map(Expression, self._expressionXML.findall('./expression')))

    @property
    def op(self):
        return self._op

    @property
    def expressions(self):
        return self._expressions

    def __str__(self):
        if self.op in Expression._LOGICALS:
            return (" " + self.op + " ").join(map(str, self._expressions))
        if self.op in Expression._COMPARISONS:
            return f"{self._expressions[0]} {self.op} {self._expressions[1]}"
        if len(self._expressions) == 0:
            return f"{self.op}"
        return "ERROR"
