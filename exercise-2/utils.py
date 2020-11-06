import numpy as np
import matplotlib.pyplot as plt

def gaussian_distribution(x,sigma,mu):
    return 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x - mu)**2 / (2 * sigma**2) )

# Sigmoid activation function
def sigmoid(x):
    return np.power(1+np.exp(-x),-1)

# ReLU activation function
def relu(x):
    return max(0.0,x)

# mean-square error loss function
def mse(observed, predicted):
    y = np.subtract(observed-predicted)
    y = np.square(y)
    return np.mean(y)

def initialize_weights():
    mu, sigma = 0, 1 
    w = np.random.normal(mu,sigma,1000)
    b = 0
    return w, b

def model(train_x, train_y, test_x, train):
    return

def train(x,y,batch_size,learning_rate):
    return history

def evaluate(x,y,):
    return loss, accuracy
