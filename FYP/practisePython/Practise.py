from __future__ import print_function
import os, sys, time, datetime, json, random    #json is a very common data format for storing information
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import SGD , Adam, RMSprop
from keras.layers.advanced_activations import PReLU
import matplotlib.pyplot as plt
import time





maze = np.array([
    [ 0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
    [ 0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.],
    [ 0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.],
    [ 1.,  1.,  0.,  1.,  1.,  0.,  1.,  0.,  0.,  0.],
    [ 0.,  0.,  1.,  0.,  1.,  0.,  1.,  1.,  1.,  0.],
    [ 0.,  0.,  1.,  0.,  1.,  0.,  0.,  0.,  0.,  0.],
    [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
    [ 0.,  0.,  0.,  0.,  0.,  0.,  1.,  1.,  1.,  1.],
    [ 0.,  1.,  1.,  1.,  1.,  1.,  0.,  0.,  0.,  0.],
    [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.]
])

#Note the usual Numpy row and column numbering conventions: each cell is represented by a pair of integers (row, col)
# where row is the row number (counted from the top!) and col is the column number (counted left to right).

#We have exactly 4 actions which we must encode as integers 0-3:
#0 - left
#1 - up
#2 - right
#3 - down

#Our rewards will be floating points ranging from -1.0 to 1.0 and each move from one state to the next state will be rewarded by a positive or a negative (penalty) amount.

