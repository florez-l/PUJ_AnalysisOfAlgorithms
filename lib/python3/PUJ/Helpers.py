## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import random

'''
--------------------------------------------------------------------------
IsSorted: Informs if a sequence is sorted
--------------------------------------------------------------------------
'''
def IsSorted( S ):
  r = False
  if( all( S[ i ] <= S[ i + 1 ] for i in range( len( S ) - 1 ) ) ):
    r = True
  # end if
  return r
# end def

'''
--------------------------------------------------------------------------
QuickAux: sorts a subsequence of comparable (<) elements
@inputs: S, a reference to a secuence of comparable elements.
         p, start of the subsequence
         r, end of the subsequence
@outputs: S[p:r], an ordered permutation of the input.
--------------------------------------------------------------------------
'''
def Partition( S, p, r ):
  x = S[ r ]
  i = p
  for j in range( p, r ):
    if S[ j ] < x:
      S[ i ], S[ j ] = S[ j ], S[ i ]
      i += 1
    # end if
  # end for
  S[ i ], S[ r ] = S[ r ], S[ i ]
  return i
# end def

'''
--------------------------------------------------------------------------
QuickAux: sorts a subsequence of comparable (<) elements
@inputs: S, a reference to a secuence of comparable elements.
         p, start of the subsequence
         r, end of the subsequence
@outputs: S[p:r], an ordered permutation of the input.
--------------------------------------------------------------------------
'''
def RandomizedPartition( S, p, r ):
  i = random.randint( p, r )
  S[ r ], S[ i ] = S[ i ], S[ r ]
  return Partition( S, p, r )
# end def

## eof - $RCSfile$
