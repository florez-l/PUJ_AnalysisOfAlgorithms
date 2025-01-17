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
  print( '{:.4e}'.format( ns * 1e-9 ), end = ' ' )
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

print( 'size ', end = '' )
for a in A:
  if a in algorithms:
    print( a, end = ' ' )
  # end if
# end for
print( '' )

# Process data
for n in range( 0, size + 1, step ):
  print( str( n ) + ' ', end = '' )
  for a in A:
    if a in algorithms:
      test_sort( S[ 0: n ], algorithms[ a ] )
    # end if
  # end for
  print( '' )
# end for

## eof - $RCSfile$
