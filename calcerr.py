import numpy as np


def MSE(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def FN(y_true, y_pred):
    return np.sqrt(np.sum(np.square(y_true - y_pred)))
