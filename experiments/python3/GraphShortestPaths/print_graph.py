## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import graphviz, math, sys

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

dot = graphviz.Digraph( comment = sys.argv[ 1 ] )
for i in range( len( G[ 0 ] ) ):
  dot.node( str( i ), G[ 0 ][ i ] )
# end for

for i in range( len( G[ 0 ] ) ):
  for j in range( len( G[ 0 ] ) ):
    if G[ 1 ][ i ][ j ] != math.inf:
      dot.edge( str( i ), str( j ), label = str( G[ 1 ][ i ][ j ] ) )
    # end if
  # end for
# end for

print( dot.source )

## eof - print_graph.py
