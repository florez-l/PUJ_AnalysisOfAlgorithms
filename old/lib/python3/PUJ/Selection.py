## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import PUJ.Helpers, PUJ.Sorting

'''
----------------------------------------------------------------------------
Naive: Selects the k-th statistic
@inputs: S, a reference to a secuence of comparable elements.
         k, the statistic position
@outputs: The k-th statistic
----------------------------------------------------------------------------
'''
def Naive( S, k ):
  if k < len( S ):
    PUJ.Sorting.Quick( S )
    return S[ k ]
  else:
    return None
  # end if
# end def

'''
----------------------------------------------------------------------------
DC: Selects the k-th statistic
@inputs: S, a reference to a secuence of comparable elements.
         k, the statistic position
@outputs: The k-th statistic
----------------------------------------------------------------------------
'''
def DC( S, k, p = 0, e = -1 ):
  if e < 0:
    r = len( S ) - 1
  else:
    r = e
  # end if

  if p <= k and k <= r:
    if p >= r:
      return S[ p ]
    else:
      q = PUJ.Helpers.RandomizedPartition( S, p, r )
      if k < q:
        return DC( S, k, p, q - 1 )
      elif k > q:
        return DC( S, k, q + 1, r )
      else:
        return S[ q ]
      # end if
    # end if
  else:
    return None
  # end if
# end def

'''
----------------------------------------------------------------------------
DC5: Selects the k-th statistic
@inputs: S, a reference to a secuence of comparable elements.
         k, the statistic position
@outputs: The k-th statistic
----------------------------------------------------------------------------
'''
def DC5( S, k, p = 0, e = -1 ):
  if e < 0:
    r = len( S ) - 1
  else:
    r = e
  # end if

  if p <= k and k <= r:

    # 5-sized groups
    m = []
    for i in range( p, r + 1, 5 ):
      f = i + 5
      if f > len( S ):
        f = len( S )
      # end if
      PUJ.Sorting.Insertion( S, i, f - 1 )
      m += [ S[ ( i + f ) // 2 ] ]
    # end for

    if len( m ) > 1:
      mi = S.index( DC5( m, len( m ) // 2 ) )
      S[ r ], S[ mi ] = S[ mi ], S[ r ]
      q = PUJ.Helpers.Partition( S, p, r )

      if k < q:
        return DC5( S, k, p, q - 1 )
      elif k > q:
        return DC5( S, k, q + 1, r )
      else:
        return S[ k ]
      # end if

    else:
      return S[ k ]
    # end if
  else:
    return None
  # end if
# end def

## eof - $RCSfile$
