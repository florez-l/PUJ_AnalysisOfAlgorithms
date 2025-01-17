## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

'''
'''
def Mode_Naive( S ):

  mode = S[ 0 ]
  count = 0

  for i in range( len( S ) ):
    c = 0
    for j in range( len( S ) ):
      if S[ j ] == S[ i ]:
        c += 1
      # end if
    # end for

    if count < c:
      mode = S[ i ]
      count = c
    # end if
  # end for

  return ( mode, count )
# end def

'''
'''
def Mode_DC_Aux( S, b, e ):
  if b >= e:
    return ( S[ b ], 1 )
  else:
    q = ( b + e ) // 2

    l = Mode_DC_Aux( S, b, q - 1 )
    r = Mode_DC_Aux( S, q + 1, e )
    if l[ 1 ] > r[ 1 ]:
      r = l
    # end if

    # Conquer
    c = 0
    for j in range( len( S ) ):
      if S[ j ] == S[ q ]:
        c += 1
      # end if
    # end for

    if c > r[ 1 ]:
      r = ( S[ q ], c )
    # end if

    return r
  # end if
# end def

'''
'''
def Mode_DC( S ):
  return Mode_DC_Aux( S, 0, len( S ) - 1 )
# end def

# --------------------------------------------------------------------------
S = [ 1, 2, 1, 12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 23, 54, 32, 43, 6, 56, 7, 56, 1 ]
print( Mode_Naive( S ) )
print( Mode_DC( S ) )

## eof - $RCSfile$
