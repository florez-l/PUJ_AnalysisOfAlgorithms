## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import math
import PUJ.Helpers

'''
----------------------------------------------------------------------------
Insertion: sorts a sequence of comparable (<) elements
@inputs: S, a reference to a secuence of comparable elements.
@outputs: S, an ordered permutation of the input.
----------------------------------------------------------------------------
'''
def Insertion( S, b = 0, e = -1 ):
# end def

'''
----------------------------------------------------------------------------
Quick: sorts a sequence of comparable (<) elements
@inputs: S, a reference to a secuence of comparable elements.
@outputs: S, an ordered permutation of the input.
----------------------------------------------------------------------------
'''
class Quick:

  # ------------------------------------------------------------------------
  # Sort: sorts a subsequence of comparable (<) elements
  # @inputs: S, a reference to a secuence of comparable elements.
  #         p, start of the subsequence
  #         r, end of the subsequence
  # @outputs: S[p:r], an ordered permutation of the input.
  # ------------------------------------------------------------------------
  def Sort( S, p, r ):
    if p < r:
      q = PUJ.Helpers.RandomizedPartition( S, p, r )
      Quick.Sort( S, p, q - 1 )
      Quick.Sort( S, q + 1, r )
    # end if
  # end def

  # ------------------------------------------------------------------------
  # Main method: sorts a sequence of comparable (<) elements
  # @inputs: S, a reference to a secuence of comparable elements.
  # @outputs: S, an ordered permutation of the input.
  # ------------------------------------------------------------------------
  def __init__( self, S ):
    Quick.Sort( S, 0, len( S ) - 1 )
  # end def
# end class

'''
----------------------------------------------------------------------------
Merge: sorts a sequence of comparable (<) elements
@inputs: S, a reference to a secuence of comparable elements.
@outputs: S, an ordered permutation of the input.
----------------------------------------------------------------------------
'''
class Merge:

  # ------------------------------------------------------------------------
  # Finish: merge two sorted sequences
  # @inputs: S, a reference to a secuence of comparable elements.
  #         p, start of the subsequence
  #         q, a pivot
  #         r, end of the subsequence
  # @outputs: S[p:r], an ordered permutation of the input.
  # ------------------------------------------------------------------------
  def Finish( S, p, q, r ):
    L = S[ p : q + 1 ] + [ math.inf ]
    R = S[ q + 1 : r + 1 ] + [ math.inf ]
    i = 0
    j = 0
    for k in range( p, r + 1 ):
      if L[ i ] < R[ j ]:
        S[ k ] = L[ i ]
        i += 1
      else:
        S[ k ] = R[ j ]
        j += 1
      # end if
    # end for
  # end def

  # ------------------------------------------------------------------------
  # Sort: sorts a subsequence of comparable (<) elements
  # @inputs: S, a reference to a secuence of comparable elements.
  #         p, start of the subsequence
  #         r, end of the subsequence
  # @outputs: S[p:r], an ordered permutation of the input.
  # ------------------------------------------------------------------------
  def Sort( S, p, r ):
    if p < r:
      q = ( p + r ) // 2
      Merge.Sort( S, p, q )
      Merge.Sort( S, q + 1, r )
      Merge.Finish( S, p, q, r )
    # end if
  # end def

  # ------------------------------------------------------------------------
  # Main method: sorts a sequence of comparable (<) elements
  # @inputs: S, a reference to a secuence of comparable elements.
  # @outputs: S, an ordered permutation of the input.
  # ------------------------------------------------------------------------
  def __init__( self, S ):
    Merge.Sort( S, 0, len( S ) - 1 )
  # end def
# end class

## eof - $RCSfile$
