## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import graphviz

"""
"""
class BinaryTree:
  m_V = None
  m_L = None
  m_R = None

  '''
  '''
  def __init__( self, v ):
    self.m_V = v
    self.m_L = None
    self.m_R = None
  # end def

  '''
  '''
  def set_left( self, n ):
    self.m_L = n
  # end def

  '''
  '''
  def set_right( self, n ):
    self.m_R = n
  # end def

  '''
  '''
  def height( self ):
    l, r = 0, 0

    if not self.m_L is None:
      l = self.m_L.height( )
    # end if

    if not self.m_R is None:
      r = self.m_R.height( )
    # end if

    return 1 + max( l, r )
  # end def

  '''
  '''
  def weight( self ):
    l, r = 0, 0

    if not self.m_L is None:
      l = self.m_L.weight( )
    # end if

    if not self.m_R is None:
      r = self.m_R.weight( )
    # end if

    return 1 + l + r
  # end def

  '''
  '''
  def __str__helper__( self, dot ):
    dot.node( str( self.m_V ), str( self.m_V ) )
    if not self.m_L is None:
      self.m_L.__str__helper__( dot )
      dot.edge( str( self.m_V ), str( self.m_L.m_V ) )
    # end if
    if not self.m_R is None:
      self.m_R.__str__helper__( dot )
      dot.edge( str( self.m_V ), str( self.m_R.m_V ) )
    # end if
  # end def

  '''
  '''
  def __str__( self ):
    dot = graphviz.Digraph( 'BinarySearchTree' )
    self.__str__helper__( dot )
    return dot.source
  # end def
# end class

## eof - $RCSfile$
