## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

'''
'''
def MatrixChain_Naive_Aux( D, i, j ):
  if i == j:
    return 0
  else:
    q = 0
    for k in range( i, j ):
      v  = MatrixChain_Naive_Aux( D, i, k )
      v += MatrixChain_Naive_Aux( D, k + 1, j )
      v += D[ i - 1 ] * D[ k ] * D[ j ]
      if k == i or v < q:
        q = v
      # end if
    # end for
    return q
  # end if
# end def

'''
'''
def MatrixChain_Naive( D ):
  return MatrixChain_Naive_Aux( D, 1, len( D ) - 1 )
# end def

'''
'''
def MatrixChain_Memoized_Aux( D, i, j, M ):
  if M[ i ][ j ] == None:
    if i == j:
      M[ i ][ j ] = 0
    else:
      q = 0
      for k in range( i, j ):
        v  = MatrixChain_Memoized_Aux( D, i, k, M )
        v += MatrixChain_Memoized_Aux( D, k + 1, j, M )
        v += D[ i - 1 ] * D[ k ] * D[ j ]
        if k == i or v < q:
          q = v
        # end if
      # end for
      M[ i ][ j ] = q
    # end if
  # end if
  return M[ i ][ j ]
# end def

'''
'''
def MatrixChain_Memoized( D ):
  M = [ [ None for j in range( len( D ) ) ] for i in range( len( D ) ) ]
  return MatrixChain_Memoized_Aux( D, 1, len( D ) - 1, M )
# end def

'''
'''
def MatrixChain_BottomUp_Backtracking( B, i, j ):
  if i == j:
    return 'A_' + str( i )
  else:
    l = MatrixChain_BottomUp_Backtracking( B, i, B[ i ][ j ] )
    r = MatrixChain_BottomUp_Backtracking( B, B[ i ][ j ] + 1, j )
    return '(' + l + ')(' + r + ')'
  # end if
# end def

'''
'''
def MatrixChain_BottomUp( D ):
  M = [ [ 0 for j in range( len( D ) ) ] for i in range( len( D ) ) ]
  B = [ [ 0 for j in range( len( D ) ) ] for i in range( len( D ) ) ]

  for i in range( len( D ) - 1, 0, -1 ):
    for j in range( i + 1, len( D ) ):
      q = 0
      p = 0
      for k in range( i, j ):
        v  = M[ i ][ k ] + M[ k + 1 ][ j ] + D[ i - 1 ] * D[ k ] * D[ j ]
        if k == i or v < q:
          q = v
          p = k
        # end if
      # end for
      M[ i ][ j ] = q
      B[ i ][ j ] = k
    # end for
  # end for

  return ( M[ 1 ][ len( D ) - 1 ], MatrixChain_BottomUp_Backtracking( B, 1, len( D ) - 1 ) )
# end def

D = [ 50, 75, 100, 2, 4, 5, 6, 7, 8, 9, 10, 100, 5, 2 ]
print( MatrixChain_Naive( D ) )
print( MatrixChain_Memoized( D ) )
print( MatrixChain_BottomUp( D ) )
