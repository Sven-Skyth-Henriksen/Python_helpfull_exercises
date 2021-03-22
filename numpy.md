# Numpy 

## Let's do it

```
import numpy as np
```

```python
import numpy as np

python_list = [[[1, 2, 3, 4], [4, 5, 6, 7]], [
    [1, 2, 3, 4], [4, 5, 6, 7]], [[1, 2, 3, 4], [4, 5, 6, 7]]]
np.array(python_list).shape

arr = np.array(python_list)
print(arr)
>>> array([[[1, 2, 3, 4],
            [4, 5, 6, 7]],

           [[1, 2, 3, 4],
            [4, 5, 6, 7]],

           [[1, 2, 3, 4],
            [4, 5, 6, 7]]])

print(arr[:, 1, 2])
>>> array([6, 6, 6])
```

