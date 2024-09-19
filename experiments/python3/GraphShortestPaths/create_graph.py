## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import math, random, sys

# Arguments
if len( sys.argv ) < 3:
  print( "Usage: python "
         +
         sys.argv[ 0 ]
         +
         " number_of_vertices connection_probability"
         )
  sys.exit( 1 )
# end if
n = int( sys.argv[ 1 ] )
p = float( sys.argv[ 2 ] )

# Show results
print( n )
for i in range( n ):
  for j in range( n ):
    if i != j:
      q = random.uniform( 0, 1 )
      if q <= p:
        print( i, j, random.randint( 1, 100 ) )
      # end if
    # end if
  # end for
# end for
print( -1 )

## eof - create_graph.py
