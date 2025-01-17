## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import random

'''
Uses the last value as pivot and put the appropriate value in its position
@input    S a reference to a secuence of comparable elements.
@optional p first index
@optional r last index
@output   a pivot value with the appropriate value in its position
@complexity O(|S|)
'''
def Partition( S, p, r ):
  x = S[ r ]
  i = p - 1

  for j in range( p, r ):
    if S[ j ] <= x:
      i += 1
      S[ i ], S[ j ] = S[ j ], S[ i ]
    # end if
  # end for

  S[ i + 1 ], S[ r ] = S[ r ], S[ i + 1 ]
  return i + 1
# end def

'''
Finds a pivot and put the appropriate value in its position
@input    S a reference to a secuence of comparable elements.
@optional p first index
@optional r last index
@output   a pivot value with the appropriate value in its position
@complexity O(|S|)
'''
def RandomizedPartition( S, p, r ):
  i = random.randint( p, r )
  S[ r ], S[ i ] = S[ i ], S[ r ]
  return Partition( S, p, r )
# end def

'''
Sorts a sequence of comparable (<) elements
@input    S a reference to a secuence of comparable elements.
@optional b first index
@optional e one past last index
@output   S an ordered permutation of the input.
@complexity Th(|S|.log2(|S|)), O(|S|^2)
'''
def Quick( S, b = -1, e = -1 ):
  r = e
  if e < 0:
    r = len( S ) - 1
  # end if
  if b < 0:
    Quick( S, 0, r )
  else:
    if b < r:

      # Pivot
      q = RandomizedPartition( S, b, r )

      # Recursive problems
      Quick( S, b, q - 1 )
      Quick( S, q + 1, r )

    # end if
  # end if
# end def

## eof - $RCSfile$
