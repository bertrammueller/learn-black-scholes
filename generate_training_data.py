from data_generator import *
import os

n_samples = 1000000
tdg = DataGenerator()
X = tdg.generate_random_input(n_samples)    # X is input matrix [ samples x inputvector ]
Y = tdg.generate_output(X)

dirname = os.path.dirname(os.path.realpath(__file__))
np.save(dirname + '/input_data', X)
np.save(dirname + '/output_data', Y)

