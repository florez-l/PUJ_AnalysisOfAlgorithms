## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import pprint

'''
'''
def LCS_Naive_Aux( X, Y, i, j ):
  if i == 0 or j == 0:
    return 0
  else:
    if X[ i - 1 ] == Y[ j - 1 ]:
      return LCS_Naive_Aux( X, Y, i - 1, j - 1 ) + 1
    else:
      a = LCS_Naive_Aux( X, Y, i - 1, j )
      b = LCS_Naive_Aux( X, Y, i, j - 1 )
      if a > b:
        return a
      else:
        return b
      # end if
    # end if
  # end if
# end def

'''
'''
def LCS_Naive( X, Y ):
  return LCS_Naive_Aux( X, Y, len( X ), len( Y ) )
# end def

'''
'''
def LCS_Memoized_Aux( X, Y, i, j, C ):
  if C[ i ][ j ] == None:
    if i == 0 or j == 0:
      C[ i ][ j ] = 0
    else:
      if X[ i - 1 ] == Y[ j - 1 ]:
        C[ i ][ j ] = LCS_Memoized_Aux( X, Y, i - 1, j - 1, C ) + 1
      else:
        a = LCS_Memoized_Aux( X, Y, i - 1, j, C )
        b = LCS_Memoized_Aux( X, Y, i, j - 1, C )
        if a > b:
          C[ i ][ j ] = a
        else:
          C[ i ][ j ] = b
        # end if
      # end if
    # end if
  # end if
  return C[ i ][ j ]
# end def

'''
'''
def LCS_Memoized( X, Y ):
  C = [ [ None for j in range( len( Y ) + 1 ) ] for i in range( len( X ) + 1 ) ]
  return LCS_Memoized_Aux( X, Y, len( X ), len( Y ), C )
# end def

'''
'''
def LCS_BottomUp( X, Y ):
  C = [ [ 0 for j in range( len( Y ) + 1 ) ] for i in range( len( X ) + 1 ) ]
  B = [ [ ( 0, 0 ) for j in range( len( Y ) + 1 ) ] for i in range( len( X ) + 1 ) ]

  for i in range( 1, len( X ) + 1 ):
    for j in range( 1, len( Y ) + 1 ):
      if X[ i - 1 ] == Y[ j - 1 ]:
        C[ i ][ j ] = C[ i - 1 ][ j - 1 ] + 1
        B[ i ][ j ] = ( -1, -1 )
      else:
        a = C[ i - 1 ][ j ]
        b = C[ i ][ j - 1 ]
        if a > b:
          C[ i ][ j ] = a
          B[ i ][ j ] = ( -1, 0 )
        else:
          C[ i ][ j ] = b
          B[ i ][ j ] = ( 0, -1 )
        # end if
      # end if
    # end for
  # end for

  # Backtrack
  i, j = len( X ), len( Y )
  Z = [ None for i in range( C[ i ][ j ] ) ]
  k = C[ i ][ j ]
  while i > 0 and j > 0:
    d = B[ i ][ j ]
    if d == ( -1, -1 ):
      k -= 1
      Z[ k ] = X[ i - 1 ]
    # end if
    i += d[ 0 ]
    j += d[ 1 ]
  # end while
  return Z
# end def

'''
--------------------- MAIN ---------------------
'''
X = 'focasowxyzcasado'
Y = 'locaseodecosas'

print( LCS_Naive( X, Y ) )
print( LCS_Memoized( X, Y ) )
print( '"' + ''.join( c for c in LCS_BottomUp( X, Y ) ) + '"' )
print( '"' + ''.join( c for c in LCS_BottomUp( 'anita lava la tina', 'dabale arroz a la zorra el abad' ) ) + '"' )

## eof - $RCSfile$
