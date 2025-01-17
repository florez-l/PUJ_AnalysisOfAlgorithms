## =========================================================================
## @author Leonardo Florez-Valencia
## =========================================================================

import random, time

## -------------------------------------------------------------------------
def MaximumSubArray_Naive( A ):
  g = 0
  b, e = 0, 0
  for i in range( len( A ) - 1 ):
    for j in range( i + 1, len( A ) ):
      d = A[ j ] - A[ i ]
      if g < d or ( i == 0 and j == 1 ):
        g, b, e = d, i, j
      # end if
    # end for
  # end for
  return ( g, ( b, e ) )
# end def

## -------------------------------------------------------------------------
def MaximumSubArray_DC_Aux( D, b, e ):
  if e <= b:
    return ( D[ b ], ( b, b + 1 ) )
  else:
    q = ( b + e ) // 2
    l = MaximumSubArray_DC_Aux( D, b, q - 1 )
    r = MaximumSubArray_DC_Aux( D, q + 1, e )
    if r[ 0 ] < l[ 0 ]:
      r = l
    # end if

    # MaximumSubArray_DC_Cross( D, b, q, e )
    li = q
    ls = D[ q ]
    s = 0
    for i in range( q, 0, -1 ):
      s += D[ i ]
      if ls < s:
        ls = s
        li = i
      # end if
    # end for

    ri = q + 1
    rs = D[ q + 1 ]
    s = 0
    for i in range( q + 1, e + 1 ):
      s += D[ i ]
      if rs < s:
        rs = s
        ri = i
      # end if
    # end for

    if r[ 0 ] < ls + rs:
      r = ( ls + rs, ( li, ri + 1 ) )
    # end if

    return r
  # end if
# end def

## -------------------------------------------------------------------------
def MaximumSubArray_DC( A ):
  D = [ A[ i ] - A[ i - 1 ] for i in range( 1, len( A ) ) ]
  return MaximumSubArray_DC_Aux( D, 0, len( D ) - 1 )
# end def

## -------------------------------------------------------------------------
def test_MaximumSubArray( A, f ):
  s = time.time( )
  r = f( A )
  e = time.time( )
  return ( r, ( e - s ) )
# end def

## -------------------------------------------------------------------------
A = [ 100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97 ]
print( test_MaximumSubArray( A, MaximumSubArray_Naive ) )
print( test_MaximumSubArray( A, MaximumSubArray_DC ) )
print( '-------------------------------------------------' )

A = [ random.randint( 1, 2e20 ) for i in range( 20000 ) ]
print( test_MaximumSubArray( A, MaximumSubArray_Naive ) )
print( test_MaximumSubArray( A, MaximumSubArray_DC ) )
print( '-------------------------------------------------' )

## eof - MaximumSubArray.py
