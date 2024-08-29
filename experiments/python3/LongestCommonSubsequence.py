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
          B[ i ][ j ] = ( 0, -1 )
        else:
          C[ i ][ j ] = b
          B[ i ][ j ] = ( -1, 0 )
        # end if
      # end if
    # end for
  # end for

  pprint.pprint( B )

  Z = []
  i, j = len( X ), len( Y )
  while i > 0 and j > 0:
    print( i, j, B[ i ][ j ] )
    if B[ i ][ j ] == ( -1, -1 ):
      print( 'ok' )
      Z += [ X[ i - 1 ] ]
    # end if
    i += B[ i ][ j ][ 0 ]
    j += B[ i ][ j ][ 1 ]
  # end while
  
  return ( C[ len( X ) ][ len( Y ) ], Z )
# end def

X = 'ocaso'
Y = 'casa'

print( LCS_Naive( X, Y ) )
print( LCS_Memoized( X, Y ) )
print( LCS_BottomUp( X, Y ) )
#print( LCS_BottomUp( 'anita lava la tina', 'dabale arroz a la zorra el abad' ) )
