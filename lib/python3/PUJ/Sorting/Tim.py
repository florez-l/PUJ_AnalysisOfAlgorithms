## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

'''
Sorts a sequence of comparable (<) elements
@input  S a reference to a secuence of comparable elements.
@optional b first index
@optional e one past last index
@output   S an ordered permutation of the input.
@complexity O(?)
'''
def Tim( S, b = -1, e = -1 ):
  r = e
  if e < 0:
    r = len( S ) - 1
  # end if
  if b < 0:
    Tim( S, 0, r )
  else:
    R = sorted( S[ b : r + 1 ] )
    for i in range( len( R ) ):
      S[ b + i ] = R[ i ]
    # end for
  # end if
# end def

## eof - $RCSfile$
