# Numpy 

## Let's do it

```
import numpy as np
```

```python
import numpy as np

python_list = [[[1, 2, 3, 4], [1, 2, 3, 4]], [
    [1, 2, 3, 4], [1, 2, 3, 4]], [[1, 2, 3, 4], [1, 2, 3, 4]]]
np.array(python_list).shape

arr = np.array(python_list)
print(arr)

print(arr[:, 1, 2])
>>> array([6, 6, 6])
```

