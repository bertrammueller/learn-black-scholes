from math import sqrt, exp, log, erf
import numpy as np

#   Generate data samples
#   We resolve dependent parameters strike and underlying price to ratio strike/underlying
class DataGenerator():

    def generate_random_input(self, n):
        ratio_strike_underlying = np.random.uniform(0.5, 1.5, n) # K/S
        time = np.random.uniform(0, 220, n)                      # time until expiration in days
        rate = np.random.uniform(0.8, 1.2, n)                    # Annualized risk free rate
        sigma = np.random.uniform(0.01, 2.0, n)                  # Standard Deviation of stock's returns
        dividend = np.random.uniform(0.8, 1.2, n)                # Dividend yield
        return np.matrix([ratio_strike_underlying, time, rate, sigma, dividend]).transpose()

    def calc_black_scholes(self, x):
        # shorthanded
        ratio_strike_underlying = x[0]
        time = x[1]
        rate = x[2]
        sigma = x[3]
        dividend = x[4]

        sigTsquared = sqrt(time / 365) * sigma
        edivT = exp((-dividend * time) / 365)
        ert = exp((-rate * time) / 365)
        d1 = (log(edivT/ratio_strike_underlying) + (rate + .5 * (sigma ** 2)) * time / 365) / sigTsquared
        d2 = d1 - sigTsquared
        Nd1 = (1 + erf(d1 / sqrt(2))) / 2
        Nd2 = (1 + erf(d2 / sqrt(2))) / 2

        # We are only interested in ratio of premium to underlying price
        ratio_call_premium_underlying = edivT*Nd1 - ratio_strike_underlying * ert * Nd2

        return ratio_call_premium_underlying

    def generate_output(self, input_data):
        return np.apply_along_axis(self.calc_black_scholes, axis=1, arr=input_data)