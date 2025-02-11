## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

'''
Sorts a sequence of comparable (<) elements
@input    S a reference to a secuence of comparable elements.
@optional b first index
@optional e one past last index
@output   S an ordered permutation of the input.
@complexity O(|S|^2)
'''
def Bubble( S, b = 0, e = -1 ):
  r = e
  if e < 0:
    r = len( S )
  # end if
  for j in range( b, r ):
    for i in range( r - 1 - j ):
      if S[ i + 1 ] < S[ i ]:
        S[ i ], S[ i + 1 ] = S[ i + 1 ], S[ i ]
      # end if
    # end for
  # end for
# end def

## eof - $RCSfile$
