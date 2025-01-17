## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import heapq, math

'''
'''
def FloydWarshall( G ):
  n = len( G[ 0 ] )
  D = [ [ None for j in range( n ) ] for i in range( n ) ]
  B = [ [ None for j in range( n ) ] for i in range( n ) ]

  for i in range( n ):
    for j in range( n ):
      if i == j:
        D[ i ][ j ] = 0
      else:
        D[ i ][ j ] = G[ 1 ][ i ][ j ]
      # end if
      B[ i ][ j ] = i
    # end for
  # end for

  for k in range( n ):
    for i in range( n ):
      for j in range( n ):
        if D[ i ][ k ] + D[ k ][ j ] < D[ i ][ j ]:
          D[ i ][ j ] = D[ i ][ k ] + D[ k ][ j ]
          B[ i ][ j ] = k
        # end if
      # end for
    # end for
  # end for

  return B
# end def

'''
'''
def FloydWarshall_Backtrack( B, s, e ):
  if B[ s ][ e ] is None:
    return []
  else:
    if s == e:
      return [ s ]
    elif B[ s ][ e ] == s:
      return [ s, e ]
    else:
      l = FloydWarshall_Backtrack( B, s, B[ s ][ e ] )
      r = FloydWarshall_Backtrack( B, B[ s ][ e ], e )
      return l + r[ 1 : len( r ) ]
    # end if
  # end if
# end def

'''
'''
def Kruskal( G, s ):
  n = len( G[ 0 ] )
  M = [ False for i in range( n ) ]
  T = [ i for i in range( n ) ]
  Q = []

  for k in range( n ):
    if G[ 1 ][ s ][ k ] != math.inf:
      heapq.heappush( Q, ( G[ 1 ][ s ][ k ], s, k ) )
    # end if
  # end for
  M[ s ] = True

  while len( Q ) > 0:
    ( c, i, j ) = heapq.heappop( Q )

    if M[ i ] and not M[ j ]:
      M[ j ] = True
      T[ j ] = i

      for k in range( n ):
        if G[ 1 ][ j ][ k ] != math.inf:
          heapq.heappush( Q, ( G[ 1 ][ j ][ k ], j, k ) )
        # end if
      # end for
    # end if
  # end while

  return T
# end def

'''
'''
def Dijkstra( G, s ):
  n = len( G[ 0 ] )
  M = [ False for i in range( n ) ]
  T = [ i for i in range( n ) ]
  Q = [ ( float( 0 ), s, s ) ]

  while len( Q ) > 0:
    ( c, i, p ) = heapq.heappop( Q )

    if not M[ i ]:
      M[ i ] = True
      T[ i ] = p

      for j in range( n ):
        if G[ 1 ][ i ][ j ] != math.inf:
          heapq.heappush( Q, ( G[ 1 ][ i ][ j ] + c, j, i ) )
        # end if
      # end for
    # end if
  # end while

  return T
# end def

'''
'''
def SpanningTree_Backtrack( T, e ):
  P = []
  j = e
  while T[ j ] != j:
    P = [ j ] + P
    j = T[ j ]
  # end while
  P = [ j ] + P
  return P
# end def

## eof - ShortestPathAlgorithms.py
