## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import os, random, struct, sys, time
sys.path.append( os.path.join( os.getcwd( ), '../lib/python3' ) )

import PUJ.Helpers, PUJ.Selection

## -------------------------------------------------------------------------
def TestSelect( S, f, k ):
  L = S[ : ]
  s = time.time_ns( )
  v = f( L, k )
  ns = time.time_ns( ) - s
  print( ' ' + str( v ) + ' ' + str( ns ), end = '' )
# end def

## -------------------------------------------------------------------------
# Read command-line input values
if len( sys.argv ) < 5:
  print(
    'Usage: python ' + sys.argv[ 0 ] +
    ' start end step [naive] [dc] [dc5]'
    )
  sys.exit( 1 )
# end if

start_size = int( sys.argv[ 1 ] )
end_size = int( sys.argv[ 2 ] )
step_size = int( sys.argv[ 3 ] )

a_n = 'naive' in sys.argv[ 4 : ]
a_dc = 'dc' in sys.argv[ 4 : ]
a_dc5 = 'dc5' in sys.argv[ 4 : ]

# Process data
for n in range( start_size, end_size, step_size ):
  S = [ random.randint( -1000, 1000 ) for i in range( n ) ]
  k = random.randint( 0, n - 1 )

  print( str( n ) + ' ' + str( k ), end = '' )
  if a_n: TestSelect( S, PUJ.Selection.Naive, k )
  if a_dc: TestSelect( S, PUJ.Selection.DC, k )
  if a_dc5: TestSelect( S, PUJ.Selection.DC5, k )
  print( '' )
  
# end for

## eof - $RCSfile$
