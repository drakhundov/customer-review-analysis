import numpy as np

"""All singular value decomposition related functionality."""


def power_method_svd(A, num_iters=100):
    """Takes a matrix and returns a list of [u, sigma, v],
    where u and v are left and right eigvecs respectively and
    sigma is the corresponding eigval.
    NOTE: This function is not used independently. Use compute_svd instead."""
    n, m = A.shape
    svd_vals = list()
    n_eig = min(n, m)
    AtA = np.dot(np.transpose(A), A)
    for _ in range(n_eig):
        v = np.random.rand(m)
        for _ in range(num_iters):
            v = np.dot(AtA, v)
            v = v / np.linalg.norm(v)
        sigma = np.linalg.norm(np.dot(A, v))
        u = np.dot(A, v) / sigma
        A = A - sigma * np.outer(u, v)
        svd_vals.append([u, sigma, v])
    return svd_vals


def compute_svd(A, k):
    """Reduces the original matrix without losing data and
    passes it to power_method_svd. Look power_method_svd for further detail.
    """
    # Random projection P (R^{ndocs x k}) into A.
    p = np.random.rand(A.shape[1], k)
    z = np.dot(A, p)
    q, _ = np.linalg.qr(z)
    # Projecting A into Q.
    y = np.dot(q.T, A)
    y_svd = power_method_svd(y)
    for i in range(len(y_svd)):
        y_svd[i][0] = np.dot(q, y_svd[i][0])
    return y_svd


def compute_A(svd_vals):
    A = np.zeros((svd_vals[0][0].shape[0], svd_vals[0][2].shape[0]))
    for i in range(len(svd_vals)):
        A += svd_vals[i][1] * np.outer(svd_vals[i][0], svd_vals[i][2])
    return A
