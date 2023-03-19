## Cover Tree

This is a Python implementation of cover trees, a data structure for finding
nearest neighbors in a general metric space (e.g., a 3D box with periodic
boundary conditions).

Cover trees are described in two papers, for which PDF copies are included
in the `references` directory:

A. Beygelzimer, S. Kakade, & J. Langford (2006) Cover Trees for Nearest Neighbor,
23rd International Conference on Machine Learning

D. R. Karger & M. Ruhl (2002) Finding Nearest Neighbors in Growth-restricted Metrics,
34th Symposium on the Theory of Computing.

(both originate from [this](http://hunch.net/~jl/projects/cover_tree/cover_tree.html) page)


The implementation here owes a great deal to PyCoverTree, by Thomas Kollar,
Nil Geisweiller, Emanuele Olivetti, which can be found here:

http://github.com/emanuele/PyCoverTree

The API follows that of Anne M. Archibald's KD-tree implementation for scipy
(scipy.spatial.kdtree).  Other than specifying a distance function in the
constructor, this module can be used as a drop-in replacement for kdtree.
