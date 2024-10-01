## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import sys
import HuffmanTree, OptimalBinarySearchTree

if len( sys.argv ) < 3:
  print( 'Usage: python ' + sys.argv[ 0 ] + ' input.txt [opt/huf]' )
  sys.exit( 1 )
# end if

# Read message
fstr = open( sys.argv[ 1 ], mode = 'rb' )
M = fstr.read( )
fstr.close( )

# Build histograms
H = { k : 0 for k in sorted( list( set( M ) ) ) }
for t in M:
  H[ t ] += 1
# end for

# Build inputs to construct trees
T = list( H.keys( ) )
P = [ float( f ) / float( len( M ) ) for f in H.values( ) ]
Q = [ float( 0 ) for p in range( len( P ) + 1 ) ]

# Solve the problem
if sys.argv[ 2 ] == 'opt':
  oT = OptimalBinarySearchTree.build( T, P, Q )
else:
  oT = HuffmanTree.build( T, P )
# end if

print( oT.weight( ) )
print( oT.height( ) )

## eof - $RCSfile$
