import unittest
from data_generator import *

class TestDataGenerator(unittest.TestCase):
    def setUp(self):
        self.tdg = DataGenerator()

    def test_black_scholes(self):
        underlying = 100.0  # price of underlying
        strike = 102.0      # strike price
        time = 25.0         # 25 days to expiry
        r = 0.05            # 5% risk free rate
        sigma = 0.2         # 20% volatility
        dividend = 0.03     # 3% dividend yield
        x = [strike / underlying, time, r, sigma, dividend]
        call_price = 1.3038     # From http://www.fintools.com/resources/online-calculators/options-calcs/options-calculator/
        y = call_price / underlying     # normalised output
        self.assertAlmostEqual(self.tdg.calc_black_scholes(x), y, 5)
