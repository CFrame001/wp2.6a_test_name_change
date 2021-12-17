from pathlib import Path
import os
import unittest
from src.excel_tools import ExcelTools


class ExcelToolsTestCase(unittest.TestCase):
    def setUp(self):
        """Fixtures used by tests."""
        self.Root = Path(__file__).parent
        self.TestDataDir = os.path.join(self.Root, 'test_data')
        self.XlsxFilePath = os.path.join(self.TestDataDir, 'test_xls.xlsx')
        self.XlsmFilePath = os.path.join(self.TestDataDir, 'test_xlsm.xlsm')

    def test_dataframes_dictionary_from_excel_file(self):
        expected = 2
        actual = len(ExcelTools.dataframes_dictionary_from_excel_file(self.XlsmFilePath))
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
