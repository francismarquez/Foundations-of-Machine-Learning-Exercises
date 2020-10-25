import numpy as np
import matplotlib.pyplot as plt

# activation functions
def sigmoid(x):
    return np.power(1+np.exp(-x),-1)

def relu(x):
    return max(0.0,x)

def slice_dataset(data, min_val, max_val):
    for i, val in enumerate(data):
        # print(i)
        # print(val)
        if (val <= min_val) :
            if i is None: print("wala") 
            else: print(i, val)