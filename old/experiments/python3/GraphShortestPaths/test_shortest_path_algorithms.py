## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import pprint, sys
from ShortestPathAlgorithms import *

'''
'''
def Path( G, P ):
  c = 0
  N = []
  for i in range( len( P ) - 1 ):
    c += G[ 1 ][ P[ i ] ][ P[ i + 1 ] ]
    N += [ G[ 0 ][ P[ i ] ] ]
  # end for
  N += [ G[ 0 ][ P[ -1 ] ] ]
  return ( c, N )
# end def

# Arguments
if len( sys.argv ) < 2:
  print( 'Usage: python ' + sys.argv[ 0 ] + ' graph_file' )
  sys.exit( 1 )
# end if

# Read file
fin = None
try:
  fin = open( sys.argv[ 1 ] )
except IOError:
  print( 'An error occurred trying to open "' +  sys.argv[ 1 ] + '"' )
  sys.exit( 1 )
# end try
lines = fin.readlines( )
fin.close( )

# Prepare graph
n = int( lines[ 0 ] )
G = (
    [ 'v_' + str( i ) for i in range( n ) ],
    [ [ math.inf for j in range( n ) ] for i in range( n ) ]
    )

# Fill graph
for line in lines[ 1 : -1 ]:
  [ i, j, c ] = line.split( )
  G[ 1 ][ int( i ) ][ int( j ) ] = float( c )
# end for

# Compute shorests paths
B_FW = FloydWarshall( G )

for s in range( n ):
  T_K = Kruskal( G, s )
  T_D = Dijkstra( G, s )

  for e in range( n ):
    print( '-------------------' )
    print( s, e )
    fw = Path( G, FloydWarshall_Backtrack( B_FW, s, e ) )
    kr = Path( G, SpanningTree_Backtrack( T_K, e ) )
    dj = Path( G, SpanningTree_Backtrack( T_D, e ) )
    print( 'Floyd-Warshall : ' + str( fw ) )
    print( 'Kruskal        : ' + str( kr ) )
    print( 'Dijkstra       : ' + str( dj ) )
  # end for
# end for

## eof - test_shortest_path_algorithms.py
