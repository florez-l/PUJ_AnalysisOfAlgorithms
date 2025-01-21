## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

def SolveHanoi( n = 1, start = 'left', end = 'right', aux = 'middle' ):
  M = []
  if n > 0:
    if n == 1:
      M = [ ( start, end, aux ) ]
    else:
      M  = SolveHanoi( n - 1, start, aux, end )
      M += SolveHanoi( 1, start, end, aux )
      M += SolveHanoi( n - 1, aux, end, start )
    # end if
  # end if
  return M
# end def

if __name__ == '__main__':

  import sys

  n = 3
  if len( sys.argv ) > 1:
    n = int( sys.argv[ 1 ] )
  # end if
  M = SolveHanoi( n, 'tower 1', 'tower 3', 'tower 2' )
  print( len( M ) )
# end if

## eof - hanoi_solver.py
