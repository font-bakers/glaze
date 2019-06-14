import numpy as np
from glaze import render

a = np.random.randn(10, 3, 2)
b = np.random.randn(5, 3, 2)
c = np.random.randn(2, 3, 2)

assert render(a)
assert render(a, b)
assert render(a, b, c)

assert render([a])
assert render([a, b])
assert render([a, b, c])
