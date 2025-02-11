## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

'''
Sorts a sequence of comparable (<) elements
@input    S a reference to a secuence of comparable elements.
@optional b first index
@optional e one past last index
@output   S an ordered permutation of the input.
@complexity O(|S|^2), Om(|S|)
'''
def Insertion( S, b = 0, e = -1 ):
  r = e
  if e < 0:
    r = len( S )
  # end if
  for j in range( b, r ):
    k = S[ j ]
    i = j - 1
    while b <= i and k < S[ i ]:
      S[ i + 1 ] = S[ i ]
      i = i - 1
    # end while
    S[ i + 1 ] = k
  # end for
# end def

## eof - $RCSfile$
