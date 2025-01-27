## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================
## Usage :
## python hanoi_solver_imperative.py [number of disks]
## =========================================================================

'''
Solve a Towers of Hanoi puzzle with n disks and start-aux-end towers.
@input n number of disks (natural).
@input (start,end,aux) identifications for each tower.
@output a sequence of movements <(from,to)> encoded with tower identificators.
'''
def SolveHanoi( n = 1, start = 'left', end = 'right', aux = 'middle' ):
  M = []
  if n == 1:
    M = [ ( start, end ) ]
  else:
    M  = SolveHanoi( n - 1, start, aux, end )
    M += SolveHanoi( 1, start, end, aux )
    M += SolveHanoi( n - 1, aux, end, start )
  # end if
  return M
# end def

'''
Print in an human readable way a sequence of Towers of Hanoi movements.
@input M a sequence of movements <(from,to)> encoded with tower identificators.
'''
def PrintHanoiSolution( M ):
  for m in M:
    print( 'move from ' + str( m[ 0 ] ) + ' to ' + str( m[ 1 ] ) )
  # end for
# end def

"""
****************************************************************************
********************************** MAIN ************************************
****************************************************************************
"""
if __name__ == '__main__':

  import sys

  n = 3
  if len( sys.argv ) > 1:
    n = int( sys.argv[ 1 ] )
  # end if
  if n < 1:
    print( 'The puzzle is not defined with a non-natural number of disks.' )
    sys.exit( 1 )
  # end if
  M = SolveHanoi( n, 'tower 1', 'tower 3', 'tower 2' )
  PrintHanoiSolution( M )
# end if

## eof - hanoi_solver_imperative.py
