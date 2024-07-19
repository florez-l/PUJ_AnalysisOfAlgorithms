## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

'''
Sorts a sequence of comparable (<) elements
@input  S a reference to a secuence of comparable elements.
@output S an ordered permutation of the input.
@complexity O(|S|^2)
'''
def Bubble( S ):
  for j in range( len( S ) ):
    for i in range( len( S ) - 1 - j ):
      if S[ i + 1 ] < S[ i ]:
        S[ i ], S[ i + 1 ] = S[ i + 1 ], S[ i ]
      # end if
    # end for
  # end for
# end def

## eof - $RCSfile$
