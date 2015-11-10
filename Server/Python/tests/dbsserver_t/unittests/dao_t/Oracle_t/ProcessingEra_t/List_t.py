"""
ProcessingEra.List unittests
"""

import os
import unittest

from dbsserver_t.utils.DaoConfig import DaoConfig
from dbsserver_t.utils.DBSDataProvider import create_dbs_data_provider, strip_volatile_fields
from dbs.dao.Oracle.ProcessingEra.List import List as ProcessingEraList

class List_t(unittest.TestCase):
    @DaoConfig("DBSReader")
    def __init__(self, methodName='runTest'):
        super(List_t, self).__init__(methodName)
        data_location = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_data.pkl')
        self.data_provider = create_dbs_data_provider(data_type='transient', data_location=data_location)
        self.data = self.data_provider.get_processing_era_data()

    def setUp(self):
        """setup all necessary parameters"""
        self.conn = self.dbi.connection()
        self.dao = ProcessingEraList(self.logger, self.dbi, self.dbowner)

    def tearDown(self):
        """Clean-up all necessary parameters"""
        self.conn.close()

    def test01(self):
        """dao.Oracle.ProcessingEra.List: Basic"""
        result = self.dao.execute(self.conn)
        self.assertTrue(isinstance(result, list))

    def test02(self):
        """dao.Oracle.ProcessingEra.List: Basic"""
        result = self.dao.execute(self.conn, processingV=self.data[0]['processing_version'])
        self.assertEqual(strip_volatile_fields(result), strip_volatile_fields(self.data))

    def test03(self):
        """dao.Oracle.ProcessingEra.List: Basic"""
        result = self.dao.execute(self.conn, -10)
        self.assertTrue(isinstance(result, list))
        self.assertEqual(len(result), 0)

if __name__ == "__main__":
    SUITE = unittest.TestLoader().loadTestsFromTestCase(List_t)
    unittest.TextTestRunner(verbosity=2).run(SUITE)
