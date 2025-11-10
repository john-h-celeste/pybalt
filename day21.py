# pluh

# numpy scipy matplotlib pandas

import numpy as np

a = np.array([[1, 2], [3, 4]])

print(a[np.where(a < 2)])
print(np.where(a < 2, a, a + 4))

# scipy is numpy but more

# scipy.linalg.solve(A, b)
# scipy.linalg.eig[envalues](A)

import scipy.integrate
import matplotlib.pyplot as plt

# numerical ode solution
def dydt(t, y):
    return -2 * y + t

sol = scipy.integrate.solve_ivp(dydt, (0, 5), [1])

plt.plot(sol.t, sol.y[0])
plt.show()

# scipy.fft

# np.random.randn[ormal](100)
# scipy.stats.skew(data)
# scipy.stats.kurtosis(data)
# t_stat,pvalue = scipy.stats.ttest_1samp(data)

# pandas

# df[col]
# df.iloc[row]
# df[df['age'] > 3]