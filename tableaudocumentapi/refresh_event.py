class RefreshEvent(object):
    """A class representing refresh events of a refresh definition inside Data Sources."""

    def __init__(self, refresh_event_xml):
        self._refresh_eventXML = refresh_event_xml
        self._add_from_file_path = refresh_event_xml.get('add-from-file-path')
        self._increment_value = refresh_event_xml.get('increment-value')
        self._refresh_type = refresh_event_xml.get('refresh-type')
        self._rows_inserted = refresh_event_xml.get('rows-inserted')
        self._timestamp_start = refresh_event_xml.get('timestamp-start')

    @property
    def add_from_file_path(self):
        return self._add_from_file_path

    @property
    def increment_value(self):
        return self._increment_value

    @property
    def refresh_type(self):
        return self._refresh_type

    @property
    def rows_inserted(self):
        return int(self._rows_inserted)

    @property
    def timestamp_start(self):
        return self._timestamp_start

    @increment_value.setter
    def increment_value(self, value):
        self._refresh_eventXML.set('increment-value', value)
        self._increment_value = value
