## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import heapq, itertools, sys

## -------------------------------------------------------------------------
class Sudoku:

  '''
  '''
  def __init__( self, N = 9 ):
    self.m_Board = [ [ 0 for j in range( N ) ] for i in range( N ) ]
  # end def

  '''
  '''
  def read( self, fname ):
    f = open( fname, 'r' )
    r = 0
    for line in f:
      c = 0
      for v in line[ : -1 ]:
        if v != 'X' and v != 'x':
          self.m_Board[ r ][ c ] = int( v )
        # end if
        c += 1
      # end for
      r += 1
    # end for
    f.close( )
  # end def

  '''
  '''
  def board( self ):
    return self.m_Board
  # end def

  '''
  '''
  def play( self, opt ):
    i = int( opt[ 0 ] )
    j = int( opt[ 1 ] )
    v = int( opt[ 2 ] )

    if i >= 9 or j >= 9 or v > 9:
      return False
    # end if

    if self.m_Board[ i ][ j ] > 0:
      return False
    # end if

    if v == 0:
      self.m_Board[ i ][ j ] = 0
      return True
    # end if

    if self.m_Board[ i ][ j ] == 0:
      self.m_Board[ i ][ j ] = -v
      if not self.is_valid( ):
        self.m_Board[ i ][ j ] = 0
        return False
      else:
        return True
      # end if
    # end if

    return False
  # end def

  '''
  '''
  def is_full( self ):
    N = len( self.m_Board )
    r = True
    for i in range( N ):
      for j in range( N ):
        if self.m_Board[ i ][ j ] == 0:
          r = False
        # end if
      # end for
    # end for
    return r
  #  end def

  '''
  '''
  def is_valid( self ):
    N = len( self.m_Board )

    # Check rows
    cr = True
    for r in range( N ):
      rows = [ 0 for i in range( N + 1 ) ]
      for j in range( N ):
        v = abs( self.m_Board[ r ][ j ] )
        rows[ v ] += 1
        if rows[ v ] > 1 and v != 0 :
          cr = False
        # end if
      # end for
    # end for

    # Check columns
    cc = True
    for c in range( N ):
      columns = [ 0 for i in range( N + 1 ) ]
      for j in range( N ):
        v = abs( self.m_Board[ j ][ c ] )
        columns[ v ] += 1
        if columns[ v ] > 1 and v != 0:
          cc = False
        # end if
      # end for
    # end for

    # Check blocks
    cb = True
    for i in range( N // 3 ):
      for j in range( N // 3 ):
        blocks = [ 0 for m in range( 10 ) ]
        for k in range( 3 * i, 3 * ( i + 1 ) ):
          for l in range( 3 * j, 3 * ( j + 1 ) ):
            v = abs( self.m_Board[ k ][ l ] )
            blocks[ v ] += 1
            if blocks[ v ] > 1 and v != 0 :
              cb = False
             # end if
          # end for
        # end for
      # end for
    # end for
    return cr and cc and cb
  # end def

  '''
  '''
  def __str__( self ):
    s  = '-+-------+-------+-------+\n'
    s += 'S| 0 1 2 | 3 4 5 | 6 7 8 |\n'
    for r in range( len( self.m_Board ) ):
      if r % 3 == 0:
        s += '-+-------+-------+-------+\n'
      # end if
      for c in range( len( self.m_Board[ r ] ) ):
        if c == 0:
          s += str( r )
        # end if
        if c % 3 == 0:
           s += '| '
        # end if
        if self.m_Board[ r ][ c ] == 0:
          s += '  '
        else:
          s += str( abs( self.m_Board[ r ][ c ] ) ) + ' '
        # end if
      # end for
      s += '|\n'
    # end for
    s += '-+-------+-------+-------+'
    return( s )
  # end def
# end class

## -------------------------------------------------------------------------
def Sudoku_human_solver( sudoku ):
  while not sudoku.is_full( ):
    print( sudoku )
    opt = input( 'Next play:' )
    if not sudoku.play( opt ):
      print( 'Invalid play' )
    # end if
  # end while
  print( sudoku )
# end def

## -------------------------------------------------------------------------
if __name__ == '__main__':

  if len( sys.argv ) < 2:
    print( 'Usage: ' + sys.argv[ 0 ] + ' input_sudoku_file' )
    sys.exit( 1 )
  # end if

  s = Sudoku( )
  s.read( sys.argv[ 1 ] )

  Sudoku_human_solver( s )

# end if

## eof - Sudoku.py
