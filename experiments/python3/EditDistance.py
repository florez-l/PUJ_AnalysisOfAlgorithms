import pprint

def EditDistance( A, B ):
  D = [ [ -1 for y in range( len( B ) + 1 ) ] for x in range( len( A ) + 1 ) ]

  for y in range( len( B ) + 1 ):
    D[ 0 ][ y ] = y
  # end for
  for x in range( len( A ) + 1 ):
    D[ x ][ 0 ] = x
  # end for

  for x in range( 1, len( A ) + 1 ):
    for y in range( 1, len( B ) + 1 ):
      if A[ x - 1 ] == B[ y - 1 ]:
        D[ x ][ y ] = D[ x - 1 ][ y - 1 ]
      else:
        c = D[ x - 1 ][ y - 1 ]
        e = D[ x - 1 ][ y ]
        i = D[ x ][ y - 1 ]
        D[ x ][ y ] = 1 + min( c, e, i )
      # end if
    # end for
  # end for
  
  return D[ len( A ) ][ len( B ) ]
# end def


print( EditDistance( "dabale arroz a la zorra el abad", "anita lava la tina" ) )
