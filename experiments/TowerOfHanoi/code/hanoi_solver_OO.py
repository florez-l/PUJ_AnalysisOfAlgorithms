## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================
## Usage :
## python hanoi_solver_OO.py [number of disks]
## =========================================================================

"""
Class that encapsulates a solver to the Towers of Hanoi puzzle.
"""
class SolveHanoi:

  '''
  Create an object with an empty movements sequence.
  '''
  def __init__( self ):
    self.m_Solution = []
  # end def

  '''
  Solve a Towers of Hanoi puzzle with n disks and start-aux-end towers.
  @input n number of disks (natural).
  @input (start,end,aux) identifications for each tower.
  @input {private} init a flag indicating that the puzzle has just started
         to be solved.
  @output the sequence of movements <(from,to)> encoded with tower
          identificators is saved in the m_Solution attribute.
  '''
  def solve(
    self, n = 1, start = 'left', end = 'right', aux = 'middle',
    init = True
    ):

    if init:
      self.m_Solution = []
    # end if

    if n == 1:
      self.m_Solution += [ ( start, end ) ]
    else:
      self.solve( n - 1, start, aux, end, init = False )
      self.solve( 1, start, end, aux, init = False )
      self.solve( n - 1, aux, end, start, init = False )
      # end if
  # end def

  '''
  Represent, in an human readable way, the sequence of Towers of Hanoi
  movements saved in the attribute m_Solution.
  '''
  def __str__( self ):
    s = ''
    for m in self.m_Solution:
      s += 'move from ' + str( m[ 0 ] ) + ' to ' + str( m[ 1 ] ) + '\n'
    # end for
    return s[ 0 : -1 ]
  # end def

# end class

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
  solver = SolveHanoi( )
  solver.solve( n, 'tower 1', 'tower 3', 'tower 2' )
  print( solver )
# end if

## eof - hanoi_solver_OO.py
