import numpy as np


def column_statistics(X):
    return X.mean(axis=0), X.std(axis=0)


def standardize(X, mean, std):
    safe_std = np.where(std == 0, 1., std)
    return (X - mean) / safe_std


def predict(X, w, b):
    return X @ w + b
