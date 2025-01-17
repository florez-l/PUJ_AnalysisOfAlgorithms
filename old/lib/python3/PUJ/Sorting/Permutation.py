## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import copy, itertools
from .Helpers import is_sorted as PUJ_Sorting_Helpers_is_sorted

'''
Sorts a sequence of comparable (<) elements
@input  S a reference to a secuence of comparable elements.
@output S an ordered permutation of the input.
@complexity O(|S|! x |S|)
'''
def Permutation( S ):
  for P in itertools.permutations( S ):
    if PUJ_Sorting_Helpers_is_sorted( P ):
      for i in range( len( P ) ):
        S[ i ] = P[ i ]
      # end for
    # end if
  # end for
# end def

## eof - $RCSfile$
