from tableaudocumentapi import RefreshEvent


class Refresh(object):
    """A class representing the refresh details inside Data Sources."""

    def __init__(self, refresh_xml):
        self._refreshXML = refresh_xml
        self._incremental_updates = refresh_xml.get('incremental-updates')
        self._increment_key = refresh_xml.get('increment-key')

        self._refresh_events = list(map(RefreshEvent, self._refreshXML.findall('./refresh-event')))

    @property
    def incremental_updates(self):
        return self._incremental_updates

    @property
    def increment_key(self):
        return self._increment_key

    @property
    def refresh_events(self):
        return self._refresh_events
