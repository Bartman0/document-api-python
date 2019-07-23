import xml.etree.ElementTree as ET
from tableaudocumentapi.dbclass import is_valid_dbclass


class Parameter(object):
    """A class representing parameters inside Data Sources."""

    def __init__(self, parmxml):
        """Parameter is usually instantiated by passing in parameter columns
        in a Data Source.
        """
        self._parameterXML = parmxml
        self._caption = parmxml.get('caption')
        self._datatype = parmxml.get('datatype')
        self._name = parmxml.get('name')
        self._param_domain_type = parmxml.get('param-domain-type')
        self._role = parmxml.get('role')
        self._type = parmxml.get('type')
        self._value = parmxml.get('value', None)

    @property
    def caption(self):
        return self._caption

    @property
    def datatype(self):
        return self._datatype

    @property
    def name(self):
        return self._name

    @property
    def param_domain_type(self):
        return self._param_domain_type

    @property
    def role(self):
        return self._role

    @property
    def type(self):
        return self._type

    @property
    def value(self):
        return self._value



