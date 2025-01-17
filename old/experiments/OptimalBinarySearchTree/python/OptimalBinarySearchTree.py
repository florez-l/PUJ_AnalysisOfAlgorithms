## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

from BinarySearchTree import BinarySearchTree

'''
'''
def _backtracking( T, B, i, j ):
  if i > j:
    return None
  else:
    n = BinarySearchTree( T[ B[ i ][ j ] - 1 ] )
    n.set_left( _backtracking( T, B, i, B[ i ][ j ] - 1 ) )
    n.set_right( _backtracking( T, B, B[ i ][ j ] + 1, j ) )
    return n
  # end if
# end def

'''
'''
def build( T, P, Q ):
  # Memoization and backtracking tables
  E = [ [ -1 for j in range( len( Q ) + 1 ) ] for i in range( len( Q ) + 1 ) ]
  B = [ [ -1 for j in range( len( Q ) + 1 ) ] for i in range( len( Q ) + 1 ) ]

  # Base cases
  for i in range( len( Q ) ):
    E[ i + 1 ][ i ] = Q[ i ]
    B[ i + 1 ][ i ] = i
  # end for

  # Iterative computations
  for i in range( len( E ) - 1, 0, -1 ):
    for j in range( i, len( E ) - 1 ):

      w = Q[ i - 1 ]
      for k in range( i, j + 1 ):
        w += P[ i - 1 ] + Q[ i ]
      # end for

      for r in range( i, j + 1 ):
        v  = w
        v += E[ i ][ r - 1 ]
        v += E[ r + 1 ][ j ]
        if E[ i ][ j ] < 0 or v < E[ i ][ j ]:
          E[ i ][ j ] = v
          B[ i ][ j ] = r
        # end if 
      # end for
    # end for
  # end for

  return  _backtracking( T, B, 1, len( P ) )
# end def

## -------------------------------------------------------------------------
if __name__ == '__main__':

  P = [ 0.15, 0.1, 0.05, 0.1, 0.2 ]
  Q = [ 0.05, 0.1, 0.05, 0.05, 0.05, 0.1 ]
  T = [ 'e1', 'e2', 'e3', 'e4', 'e5' ]
  oT = build( T, P, Q )
  print( oT )

# end if

## eof - $RCSfile$
