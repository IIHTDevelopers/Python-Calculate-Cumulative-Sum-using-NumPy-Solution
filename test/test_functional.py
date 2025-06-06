import unittest
import numpy as np
from mainclass import CumulativeSumAnalysis
from test.TestUtils import TestUtils
import pandas as pd

class FunctionalTests(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.sales_data = [10, 20, 30, 40, 50]
        self.analysis = CumulativeSumAnalysis(self.sales_data)

    def test_cumulative_sum_numpy(self):
        """Test NumPy cumulative sum"""
        result = self.analysis.cumulative_sum_numpy()
        expected_result = np.array([10, 30, 60, 100, 150], dtype=np.float32)
        test_obj = TestUtils()
        if np.array_equal(result, expected_result):
            test_obj.yakshaAssert("TestCumulativeSumNumPy", True, "functional")
            print("TestCumulativeSumNumPy = Passed")
        else:
            test_obj.yakshaAssert("TestCumulativeSumNumPy", False, "functional")
            print("TestCumulativeSumNumPy = Failed")

    def test_cumulative_sum_python(self):
        """Test Python list cumulative sum"""
        result = self.analysis.cumulative_sum_python()
        expected_result = [10, 30, 60, 100, 150]
        test_obj = TestUtils()
        if result == expected_result:
            test_obj.yakshaAssert("TestCumulativeSumPython", True, "functional")
            print("TestCumulativeSumPython = Passed")
        else:
            test_obj.yakshaAssert("TestCumulativeSumPython", False, "functional")
            print("TestCumulativeSumPython = Failed")

