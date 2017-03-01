# learn-black-scholes
Run generate_training_data.py with number of samples as command line argument.
Running this with 1e6 samples takes some time and results in 50MB of numpy binary data files.

### Install
install miniconda if not available on system

> conda create -n bsenv python=3.5
> source activate bsenv
> conda install numpy scipy scikit-learn pandas jupyter
> jupyter notebook
