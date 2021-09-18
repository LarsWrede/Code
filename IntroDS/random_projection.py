import numpy as np
import matplotlib.pyplot as plt


def random_projection_method(X, R):
    """
    Implements the random-projection methods.

    Args:
    X: data matrix (with dimensions dxN)
    R: projection matrix (with dimensions kxd, where k < d)

    Returns:
    random projection of X (with dimensions kxN)
    """
    return np.linalg.linalg.dot(R, X)


def achloptas_matrix(X):
    """
    Generates the Achlioptas projection matrix.

    Args:
    X: data matrix (with dimensions dxN)
    R: target dimension for dimensionality reduction

    Returns:
    Achlioptas matrix (with dimensions kxN)
    """
    d = X.shape()
    R = np.zeros((k, d))


X = np.ones((10, 10))
R = np.ones((10, 10))

random_projection_method(X, R)

X.shape[0]

achloptas_matrix(X, 5)

np.random.seed(10)
np.random.rand(k, d)
