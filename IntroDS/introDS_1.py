import numpy as np
import matplotlib.pyplot as plt

def johnson_lindenstrauss_min_dim(m, eps):
    return 8*np.log(m)/eps**2

eps = 0.1
m = np.arange(10,1010,10)

JL_bound = johnson_lindenstrauss_min_dim(m, eps)

plt.figure()
for eps in np.linspace(0.1,0.5):
    plt.plot(m, johnson_lindenstrauss_min_dim(m, eps), color="tab:blue")
plt.xlabel(r"number of data points")
plt.ylabel(r"JL bound")
plt.yscale("log")
plt.tight_layout()
plt.show()