import pandas as pd
import numpy as np
import numpy.matlib
from numpy import matmul
from numpy import array as matrix, arange, zeros
import sklearn
from sklearn import decomposition

def NMF(V, num_patterns, num_iterations):
    '''
    Args:
        V: numpy.array (n * m)
        num_patterns: int
        num_iterations: int

    Returns:
        W: (n * num_patterns)
        H: (num_patterns * m)
        loss: average loss
    '''
    n = V.shape[0]
    m = V.shape[1]
    r = num_patterns
    W = np.random.rand(n, r)
    H = np.random.rand(r, m)
    for it in range(num_iterations):
        print ('iteration on: ', it)
        for i in range(n):
            for j in range(m):
                for k in range(r):
                    W[i][k] *= matmul(V, H.T)[i][k] / matmul(W, matmul(H, H.T))[i][k]
                    H[k][j] *= matmul(W.T, V)[k][j] / matmul(W.T, matmul(W, H))[k][j]

    loss = 0.0
    for i in range(n):
        for j in range(m):
            for k in range(r):
                loss += V[i][j] - W[i][k] * H[k][j]

    return W, H, loss
