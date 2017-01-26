from data_generator import *
import os
import argparse

parser = argparse.ArgumentParser(description='Generate training data for black scholes.')
parser.add_argument('n', metavar='N', type=int, nargs=1, help='number of samples')

n_samples = parser.parse_args().n[0]
tdg = DataGenerator()
X = tdg.generate_random_input(n_samples)    # X is input matrix [ samples x inputvector ]
Y = tdg.generate_output(X)

dirname = os.path.dirname(os.path.realpath(__file__))
np.save(dirname + '/input_data', X)
np.save(dirname + '/output_data', Y)

