from tableaudocumentapi import DBColumn, Relation, Connection


class Extract(object):
    """A class representing extracts inside Data Sources."""

    def __init__(self, extract_xml):
        """Extract is usually instantiated by passing in extract XML
        from a Data Source.
        """
        self._extractXML = extract_xml
        self._enabled = extract_xml.get('enabled')
        self._units = extract_xml.get('units')

        self._connection = list(map(Connection, self._extractXML.findall('./connection')))
        self._relation = list(map(Relation, self._extractXML.findall('./connection/relation')))
        self._cols = list(map(DBColumn, self._extractXML.findall('./connection/cols/*')))

    @property
    def enabled(self):
        return self._enabled

    @property
    def units(self):
        return self._units

    @property
    def connection(self):
        return self._connection
