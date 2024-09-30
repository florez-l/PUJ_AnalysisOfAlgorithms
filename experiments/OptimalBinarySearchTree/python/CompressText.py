## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import itertools, re, sys, unidecode
import HuffmanTree, OptimalBinarySearchTree

if len( sys.argv ) < 3:
  print( 'Usage: python ' + sys.argv[ 0 ] + ' input.txt [opt/huf]' )
  sys.exit( 1 )
# end if

# Read message
pat = re.compile( '[\\W_]+' )
fstr = open( sys.argv[ 1 ] )
M = \
  [ \
    re.sub( pat, '', w ).lower( ) \
    for w in list( \
      itertools.chain.from_iterable( \
        [ unidecode.unidecode( l ).split( ) for l in fstr.readlines( ) ] \
        ) \
      ) \
  ]
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
  print( oT.encode( ) )
# end if

## eof - $RCSfile$
