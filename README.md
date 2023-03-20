# Cover Tree

This is a Python implementation of cover trees, a data structure for finding
nearest neighbors in a general metric space (e.g., a 3D box with periodic
boundary conditions).

Updated for Python 3.7 from [Patrick Varilly's code](https://github.com/patvarilly/CoverTree).

## Installation

```
pip install covertree
```

## Usage

The usage for CoverTree is exactly the same as for a KDTree, except you can specify your
distance metric in the constructor:

```

from scipy.spatial import KDTree
from covertree import CoverTree

import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 3D points
points = np.random.uniform(size=(1000, 3))

# Simple p-norm metric
# With power = 2, gives the exact same result as a kd-tree
power = 2
def metric(q,p):
    return (np.sum(np.abs(q - p)**power))**(1/power)

#tree = KDTree(points)
tree = CoverTree(points, metric)

# Query a ball around the center of our points
# with a radius of .2
pointsInBall = points[tree.query_ball_point(np.array([0.5, 0.5]), .2)]

plt.scatter(pointsInBall[:,0], pointsInBall[:,1])
plt.show()

```

As above, you can define your own metric (function that takes two points as arguments and returns
a scalar) or you can use any of the predefined ones in [scipy.spatial.distance](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html).

As of now, this cover tree is not nearly as fast as the scipy's KDTree; optimization is currently
in progress for the library.

![Benchmark of tree construction time](https://raw.githubusercontent.com/Jfeatherstone/CoverTree/master/images/benchmark_construction.png)

The implementation here owes a great deal to [PyCoverTree](http://github.com/emanuele/PyCoverTree),
by Thomas Kollar, Nil Geisweiller, Emanuele Olivetti.

The API follows that of Anne M. Archibald's KD-tree implementation for scipy;
the default metric has been set to euclidean distance, so the `CoverTree` class
can be used exactly as a drop in replacement for 
[scipy.spatial.KDTree](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.html).


## References

Cover trees are described in two papers, for which PDF copies are included
in the `references` directory:

[1] D. R. Karger & M. Ruhl (2002) Finding Nearest Neighbors in Growth-restricted Metrics,
34th Symposium on the Theory of Computing.

[2] A. Beygelzimer, S. Kakade, & J. Langford (2006) Cover Trees for Nearest Neighbor,
23rd International Conference on Machine Learning

(both originate from [this](http://hunch.net/~jl/projects/cover_tree/cover_tree.html) page)

