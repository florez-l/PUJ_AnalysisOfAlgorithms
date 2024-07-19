## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import sys, time
sys.path.append( '../../lib/python3' )
import PUJ.Sorting

## -------------------------------------------------------------------------
def test_sort( S, f ):
  L = S.copy( )
  s = time.time_ns( )
  f( L )
  ns = time.time_ns( ) - s
  if not PUJ.Sorting.Helpers.is_sorted( L ):
    raise Exception( 'Sequence was not ordered!: **', f, '**' )
  # end if
  print( str( ns ), end = ',' )
# end def


## -------------------------------------------------------------------------
## ------------------------------ MAIN SCRIPT ------------------------------
## -------------------------------------------------------------------------

if len( sys.argv ) < 4:
  print(
    'Usage: python ' + sys.argv[ 0 ] +
    ' datafile size step' +
    ' [permutation] [bubble] [insertion] [quick] [merge] [tim]'
    )
  sys.exit( 1 )
# end if
datafile = sys.argv[ 1 ]
size = int( sys.argv[ 2 ] )
step = int( sys.argv[ 3 ] )

# -- Read some data
datafile_ifs = open( datafile, 'rb' )
S = list( datafile_ifs.read( ) )[ : size ]
datafile_ifs.close( )

# -- Get algoritms
algorithms = {
  'permutation' : PUJ.Sorting.Permutation,
  'bubble'      : PUJ.Sorting.Bubble,
  'insertion'   : PUJ.Sorting.Insertion,
  'quick'       : PUJ.Sorting.Quick,
  'merge'       : PUJ.Sorting.Merge,
  'tim'         : PUJ.Sorting.Tim,
  }
A = [ a.lower( ) for a in sys.argv[ 4 : ] ]

for a in A:
  if a in algorithms:
    print( a, end = ',' )
  # end if
# end for
print( '' )

for a in A:
  if a in algorithms:
    test_sort( S, algorithms[ a ] )
  # end if
# end for
print( '' )


# import os, random, struct, sys, time

# import PUJ.Helpers, PUJ.Sorting

# ## -------------------------------------------------------------------------
# def TestSort( S, f ):
#   L = S[ : ]
#   s = time.time_ns( )
#   f( L )
#   ns = time.time_ns( ) - s
#   print(
#       ' ' + str( PUJ.Helpers.IsSorted( S ) ) +
#       ' ' + str( PUJ.Helpers.IsSorted( L ) ) +
#       ' ' + str( ns ), end = ''
#       )
# # end def

# ## -------------------------------------------------------------------------
# # Read command-line input values
# if len( sys.argv ) < 5:
#   print(
#     'Usage: python ' + sys.argv[ 0 ] +
#     ' start end step [bubble] [insertion] [quick] [merge] [native]'
#     )
#   sys.exit( 1 )
# # end if

# start_size = int( sys.argv[ 1 ] )
# end_size = int( sys.argv[ 2 ] )
# step_size = int( sys.argv[ 3 ] )

# a_b = 'bubble' in sys.argv[ 4 : ]
# a_i = 'insertion' in sys.argv[ 4 : ]
# a_q = 'quick' in sys.argv[ 4 : ]
# a_m = 'merge' in sys.argv[ 4 : ]
# a_n = 'native' in sys.argv[ 4 : ]

# # Process data
# for n in range( start_size, end_size, step_size ):
#   S = [ random.randint( -1000, 1000 ) for i in range( n ) ]

#   print( n, end = '' )
#   if a_b: TestSort( S, PUJ.Sorting.Bubble )
#   if a_i: TestSort( S, PUJ.Sorting.Insertion )
#   if a_q: TestSort( S, PUJ.Sorting.Quick )
#   if a_m: TestSort( S, PUJ.Sorting.Merge )
#   if a_n: TestSort( S, PUJ.Sorting.Native )
#   print( '' )
  
# # end for

## eof - $RCSfile$
