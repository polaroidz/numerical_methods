import unittest

import numpy as np

from src import riemann
from src import trapezoid
from src import simpsons

class TestIntergrationMethods(unittest.TestCase):

    #_method = trapezoid # (places = 3)
    #_method = riemann   # (places = 4)
    _method = simpsons   # (places = 5)

    def test_circular_function_integration(self):
        a = 0.0
        b = np.pi / 2
        steps = 100
        
        res_sin = self._method.calc(np.sin, a, b, N=steps)
        res_cos = self._method.calc(np.cos, a, b, N=steps)

        self.assertAlmostEqual(res_sin, 1.0, places=5)
        self.assertAlmostEqual(res_cos, 1.0, places=5)

