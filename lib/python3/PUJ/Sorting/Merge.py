## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

'''
Sorts a sequence of comparable (<) elements
@input    S a reference to a secuence of comparable elements.
@optional b first index
@optional e one past last index
@output   S an ordered permutation of the input.
@complexity Th(|S|.log2(|S|))
'''
def Merge( S, b = -1, e = -1 ):
  r = e
  if e < 0:
    r = len( S ) - 1
  # end if
  if b < 0:
    Merge( S, 0, r )
  else:
    if b < r:

      # Pivot
      q = ( b + r ) // 2

      # Recursive problems
      Merge( S, b, q )
      Merge( S, q + 1, r )

      # Merge initialization
      L = S[ b : q + 1 ]
      R = S[ q + 1 : r + 1 ]
      i, j, k = 0, 0, b

      # Merge L and R
      while i < len( L ) and j < len( R ):
        if L[ i ] < R[ j ]:
          S[ k ] = L[ i ]
          i += 1
        else:
          S[ k ] = R[ j ]
          j += 1
        # end if
        k += 1
      # end while

      # Merge remaining L
      while i < len( L ):
        S[ k ] = L[ i ]
        i += 1
        k += 1
      # end while

      # Merge remaining R
      while j < len( R ):
        S[ k ] = R[ j ]
        j += 1
        k += 1
      # end while

    # end if
  # end if
# end def

## eof - $RCSfile$
