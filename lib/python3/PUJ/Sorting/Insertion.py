## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

'''
Sorts a sequence of comparable (<) elements
@input  S a reference to a secuence of comparable elements.
@output S an ordered permutation of the input.
@complexity O(|S|^2)
'''
def Insertion( S ):
  for j in range( len( S ) ):
    k = S[ j ]
    i = j - 1
    while 0 <= i and k < S[ i ]:
      S[ i + 1 ] = S[ i ]
      i = i - 1
    # end while
    S[ i + 1 ] = k
  # end for
# end def

## eof - $RCSfile$
