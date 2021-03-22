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

np.empty # Return a new array of given shape and type, without initializing entries.
np.zeros # Return a new array of given shape and type, filled with zeros.
np.ones # Return a new array of given shape and type, filled with ones
np.nonzero
np.eye # Return a 2-D array with ones on the diagonal and zeros elsewhere.
np.arange
np.reshape
np.random.random
np.identity
[np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace) # Return evenly spaced numbers over a specified interval
np.diag
np.pad
np.unravel_index # Converts a flat index or array of flat indices into a tuple of coordinate arrays
np.
np.






