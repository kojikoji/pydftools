import unittest
import pandas as pd
import numpy as np
import calc


class TestCalcs(unittest.TestCase):
    def test_addcolumns(self):
        df = pd.DataFrame({'x': np.arange(10), 'y': np.arange(10)})
        df = calc.add_columns(df, lambda x: np.sum(x, axis=1), ['x', 'y'], 'add')
        self.assertAlmostEqual(df['add'][9], 18)
        


if __name__ == '__main__':
    unittest.main()
