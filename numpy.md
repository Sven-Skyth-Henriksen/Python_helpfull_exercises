# Numpy 

## Let's do it

```
import numpy as np
```

```
import numpy as np

python_list = [[[1, 2, 3, 4], [1, 2, 3, 4]], [
    [1, 2, 3, 4], [1, 2, 3, 4]], [[1, 2, 3, 4], [1, 2, 3, 4]]]
np.array(python_list).shape

arr = np.array(python_list)
print(arr)

print(arr[:, 1, 2])
>>> array([6, 6, 6])

```


## Useful stuff

- [np.empty](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty) # Return a new array of given shape and type, without initializing entries.
- [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros) # Return a new array of given shape and type, filled with zeros.
- [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones) # Return a new array of given shape and type, filled with ones
- [np.nonzero](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html?highlight=nonzeros) # Return the indices of the elements that are non-zero.
- [np.eye](https://numpy.org/doc/stable/reference/generated/numpy.eye.html?highlight=eye) # Return a 2-D array with ones on the diagonal and zeros elsewhere.
- [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange) # Return evenly spaced values within a given interval.
- [np.reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html?highlight=reshape#numpy.reshape) # Gives a new shape to an array without changing its data
- [np.random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html?highlight=random%20random#numpy.random.random) # Return random floats
- [np.identity](https://numpy.org/doc/stable/reference/generated/numpy.identity.html#numpy.identity) # Return the identity array
- [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace) # Return evenly spaced numbers over a specified interval
- [np.diag](https://numpy.org/doc/stable/reference/generated/numpy.diag.html?highlight=diag#numpy.diag) # Extract a diagonal or construct a diagonal array
- np.pad
- [np.unravel_index](https://numpy.org/doc/stable/reference/generated/numpy.unravel_index.html?highlight=unravel_index#numpy.unravel_index) # Converts a flat index or array of flat indices into a tuple of coordinate arrays
- np.
- np.






