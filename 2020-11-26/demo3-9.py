import numpy as np


a = np.repeat(np.arange(5).reshape([1, -1]), 10, axis=0) + 10.0
print(a)
b = np.random.randint(5, size=a.shape)
print(b)
result = a*b
c = np.argmin(result, axis=1)
print(c)
b = np.zeros(a.shape)
print(b)
b[np.arange(b.shape[0]), c] = 1
print(b)