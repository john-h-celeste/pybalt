import numpy as np

# numpy my beloved
np.array([1, 2, 3], dtype = np.int64) # default dtype is float64

x = np.arange(12).reshape(3, 4)

print(x, x.shape, x.dtype, x[1, 2])

a = np.arange(-3, 31, 4) # just like builtin range()
s = a[2:4]
s[:] = 0 # a slice is a view and it modifies the original array
m = a[a > 7]
m[:] = -1 # a mask is a partial copy
print(a)

# zeros ones
print(np.zeros((2, 4)))
print(np.ones((2, 2), dtype = np.float32))

# combine
print(np.concatenate([np.ones((5, 3)), np.zeros((5, 2))], axis = 1))
# vstack is by axis 0 (top and bottom)
# hstack is by axis 1 (side by side)

# you can use matrix.astype(dtype)

# np.zeros_like() and np.ones_like()
# create a matrix with the same shape

print(np.random.random((4, 4))) # random float 0-1
print(np.random.randint(0, 2, (4, 4))) # random int in range not including top

# np.abs(m) / m.abs()

# m.T
# m.transpose((0, 1)) # swap two axes

np.savez('bung.npz', array = np.arange(15))
print(np.load('bung.npz'))
np.savez('bungd.npz', np.arange(15))
print(np.load('bungd.npz'))

# element wise arithmetic
# logical operators return bool array
# but there's also @ for matrix multiplication

np.sqrt
np.exp

# you can use normal indexing with multiple comma separated indices
# tuple as index selects multiple rows
print(x[1, (1, 3)])

# you can also assign to a masked section of an array
x[x > 9] = 0
print(x)

# m.sum() usually removes an axis
# keepdims = True makes it set that axis's size to 1
print(x.sum())
print(x.sum(axis = 0))
print(x.sum(axis = 1))
print(x.sum(axis = 0, keepdims = True))
print(x.sum(axis = 1, keepdims = True))

print('mean per column')
print(np.arange(12).reshape(4, 3).mean(axis = 0))


A = np.array([[1, 2], [3, 4]])
print()
print('A @ A.T')
print(A @ A.T)
print()
print('A.T @ A')
print(A.T @ A)