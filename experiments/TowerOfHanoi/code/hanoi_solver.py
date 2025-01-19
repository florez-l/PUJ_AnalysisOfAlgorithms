## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

def SolveHanoi( n = 1, start = 'left', end = 'right', aux = 'middle' ):
  if n > 0:
    if n == 1:
      print( 'move top disk from ' + str( start ) + ' to ' + str( end ) )
    else:
      SolveHanoi( n - 1, start, aux, end )
      SolveHanoi( 1, start, end, aux )
      SolveHanoi( n - 1, aux, end, start )
    # end if
  # end if
# end def

if __name__ == '__main__':

  import sys

  n = 3
  if len( sys.argv ) > 1:
    n = int( sys.argv[ 1 ] )
  # end if
  SolveHanoi( n, 'tower 1', 'tower 3', 'tower 2' )
# end if

## eof - hanoi_solver.py
