#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script: NeuralNetwork2.py

This script creates a 2-layer Neural Network.

Goal would be to predict time or reps likely to be accomplished to a new workout.

"""

import numpy

#sigmoid function
def nonlin(x, deriv = False):
    """Sigmoid Function"""
    if deriv == True:
        return x*(1-x)
    return 1/(1+numpy.exp(-x))

# Input Dataset
X = numpy.array([[1,4,7,9],
                [5,7,9,3],
                [1,1,1,1],
                [3,7,0,0]])
# Output Dataset
y = numpy.array([[21,24,4,10]]).T

# seed random numbers to make calculation deterministic
numpy.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2*numpy.random.random((len(X[0]),1)) - 1

for iter in range(10000):
    #forward propagation
    layer0 = X
    layer1 = nonlin(numpy.dot(layer0, syn0))

    # Error calculation:
    layer1_error = y - layer1

    # multiply error by slope of sigmoid at values in layer1:
    layer1_delta = layer1_error * nonlin(layer1, True)

    # Update Weights:
    syn0 += numpy.dot(layer0.T, layer1_delta)

print("Output After Training:")
print(layer1)



