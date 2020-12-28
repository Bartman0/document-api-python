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
    def test_extract_check(self):
        ds = Datasource.from_file(TEST_TDS_FILE)
        self.assertIsNotNone(ds.has_extract())

    def test_refresh_increment_key(self):
        ds = Datasource.from_file(TEST_TDS_FILE)
        self.assertEqual('[datum]', ds.extract.refresh.increment_key)

    def test_refresh_incremental_updates(self):
        ds = Datasource.from_file(TEST_TDS_FILE)
        self.assertEqual('true', ds.extract.refresh.incremental_updates)

    def test_refresh_events(self):
        ds = Datasource.from_file(TEST_TDS_FILE)
        self.assertIsNotNone(ds.extract.refresh.refresh_events)

    def test_refresh_increment_value(self):
        ds = Datasource.from_file(TEST_TDS_FILE)
        self.assertEqual(dt.datetime.strptime('2002-02-02', '%Y-%m-%d'),
                         dt.datetime.strptime(ds.extract.refresh.refresh_events[1].increment_value, '#%Y-%m-%d#'))

    def test_refresh_type(self):
        ds = Datasource.from_file(TEST_TDS_FILE)
        self.assertEqual('increment', ds.extract.refresh.refresh_events[1].refresh_type)

    def test_refresh_type(self):
        ds = Datasource.from_file(TEST_TDS_FILE)
        self.assertEqual(1, ds.extract.refresh.refresh_events[1].rows_inserted)
