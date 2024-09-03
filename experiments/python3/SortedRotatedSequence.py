## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

'''
'''
def RotationOrder_Naive( S ):
  max_i = 0
  while max_i < len( S ) - 1 and S[ max_i ] < S[ max_i + 1 ]:
    max_i += 1
  # end while
  return ( ( max_i + 1 ) % len( S ) ) + 1
# end def

'''
'''
def RotationOrder_DC_Aux( S, b, e ):
  if e <= b:
    return b
  else:
    if S[ b ] <= S[ e ]:
      return e
    else:
      q = ( b + e ) // 2
      if S[ q ] > S[ ( q + 1 ) % len( S ) ]:
        return q
      else:
        if S[ b ] <= S[ q ]:
          return RotationOrder_DC_Aux( S, q, e )
        else: # if S[ q ] <= S[ e ]:
          return RotationOrder_DC_Aux( S, b, q )
        # end if
      # end if
    # end if
  # end if
# end def

'''
'''
def RotationOrder_DC( S ):
  return ( ( RotationOrder_DC_Aux( S, 0, len( S ) - 1 ) + 1 ) % len( S ) ) + 1
# end def

# --------------------------------------------------------------------------
S = \
  [ \
    9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, \
    25, 26, 27, 1, 2 \
  ]
print( RotationOrder_Naive( S ) )
print( RotationOrder_DC( S ) )

## eof - $RCSfile$
