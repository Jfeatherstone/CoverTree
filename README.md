# Cover Tree

This is a Python implementation of cover trees, a data structure for finding
nearest neighbors in a general metric space (e.g., a 3D box with periodic
boundary conditions).

Updated for Python 3.7 from [Patrick Varilly's code](https://github.com/patvarilly/CoverTree).


The implementation here owes a great deal to [PyCoverTree](http://github.com/emanuele/PyCoverTree),
by Thomas Kollar, Nil Geisweiller, Emanuele Olivetti.

The API follows that of Anne M. Archibald's KD-tree implementation for scipy;
the default metric has been set to euclidean distance, so the `CoverTree` class
can be used exactly as a drop in replacement for 
[scipy.spatial.KDTree](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.html).


## References

Cover trees are described in two papers, for which PDF copies are included
in the `references` directory:

A. Beygelzimer, S. Kakade, & J. Langford (2006) Cover Trees for Nearest Neighbor,
23rd International Conference on Machine Learning

D. R. Karger & M. Ruhl (2002) Finding Nearest Neighbors in Growth-restricted Metrics,
34th Symposium on the Theory of Computing.

(both originate from [this](http://hunch.net/~jl/projects/cover_tree/cover_tree.html) page)

