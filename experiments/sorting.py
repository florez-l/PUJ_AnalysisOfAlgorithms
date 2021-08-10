## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import os, random, struct, sys, time
sys.path.append( os.path.join( os.getcwd( ), '../lib/python3' ) )

import PUJ.Helpers, PUJ.Sorting

## -------------------------------------------------------------------------
def TestSort( S, f ):
  L = S[ : ]
  s = time.time_ns( )
  f( L )
  ns = time.time_ns( ) - s
  print(
      ' ' + str( PUJ.Helpers.IsSorted( S ) ) +
      ' ' + str( PUJ.Helpers.IsSorted( L ) ) +
      ' ' + str( ns ), end = ''
      )
# end def

## -------------------------------------------------------------------------
# Read command-line input values
if len( sys.argv ) < 5:
  print(
    'Usage: python ' + sys.argv[ 0 ] +
    ' start end step [bubble] [insertion] [quick] [merge] [native]'
    )
  sys.exit( 1 )
# end if

start_size = int( sys.argv[ 1 ] )
end_size = int( sys.argv[ 2 ] )
step_size = int( sys.argv[ 3 ] )

a_b = 'bubble' in sys.argv[ 4 : ]
a_i = 'insertion' in sys.argv[ 4 : ]
a_q = 'quick' in sys.argv[ 4 : ]
a_m = 'merge' in sys.argv[ 4 : ]
a_n = 'native' in sys.argv[ 4 : ]

# Process data
for n in range( start_size, end_size, step_size ):
  S = [ random.randint( -1000, 1000 ) for i in range( n ) ]

  print( n, end = '' )
  if a_b: TestSort( S, PUJ.Sorting.Bubble )
  if a_i: TestSort( S, PUJ.Sorting.Insertion )
  if a_q: TestSort( S, PUJ.Sorting.Quick )
  if a_m: TestSort( S, PUJ.Sorting.Merge )
  if a_n: TestSort( S, PUJ.Sorting.Native )
  print( '' )
  
# end for

## eof - $RCSfile$
