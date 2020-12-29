import unittest
import os.path
import datetime as dt

from tableaudocumentapi import Datasource

TEST_ASSET_DIR = os.path.join(
    os.path.dirname(__file__),
    'assets'
)
TEST_TDS_FILE = os.path.join(
    TEST_ASSET_DIR,
    'test_data.tds'
)


class ExtractRead(unittest.TestCase):
    def setUp(self) -> None:
        self.ds = Datasource.from_file(TEST_TDS_FILE)

    def test_extract_check(self):
        self.assertIsNotNone(self.ds.has_extract())

    def test_refresh_increment_key(self):
        self.assertEqual('[datum]', self.ds.extract.refresh.increment_key)

    def test_refresh_incremental_updates(self):
        self.assertEqual('true', self.ds.extract.refresh.incremental_updates)

    def test_refresh_events(self):
        self.assertIsNotNone(self.ds.extract.refresh.refresh_events)

    def test_refresh_increment_value(self):
        self.assertEqual(dt.datetime.strptime('2002-02-02', '%Y-%m-%d'),
                         dt.datetime.strptime(self.ds.extract.refresh.refresh_events[1].increment_value, '#%Y-%m-%d#'))

    def test_refresh_type(self):
        self.assertEqual('increment', self.ds.extract.refresh.refresh_events[1].refresh_type)

    def test_refresh_type(self):
        self.assertEqual(1, self.ds.extract.refresh.refresh_events[1].rows_inserted)

    def test_connection_class(self):
        self.assertIsNotNone(self.ds.extract.connection.dbclass)

    def test_connection_class_hyper(self):
        self.assertEqual('hyper', self.ds.extract.connection.dbclass)

    def test_connection_dbname(self):
        self.assertEqual('/Users/rkooijman/Documents/My Tableau Repository/Datasources/test_data (postgres).hyper',
                         self.ds.extract.connection.dbname)

    def test_connection_dbname(self):
        self.assertEqual('/Users/rkooijman/Documents/My Tableau Repository/Datasources/test_data (postgres).hyper',
                         self.ds.extract.connection.dbname)

    def test_connection_schema(self):
        self.assertEqual('Extract',
                         self.ds.extract.connection.schema)

    def test_set_last_refresh_increment_value(self):
        filename = os.path.join(TEST_ASSET_DIR, 'set_last_refresh_increment_value.tds')
        newdate = '#2003-03-03#'

        self.ds.extract.refresh.refresh_events[-1].increment_value = newdate
        try:
            self.ds.save_as(filename)
            ds_new = Datasource.from_file(filename)
            self.assertEqual(dt.datetime.strptime(newdate, '#%Y-%m-%d#'),
                             dt.datetime.strptime(ds_new.extract.refresh.refresh_events[1].increment_value, '#%Y-%m-%d#'))
        finally:
            if os.path.exists(filename):
                os.unlink(filename)
