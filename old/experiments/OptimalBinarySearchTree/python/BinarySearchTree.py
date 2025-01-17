## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

from BinaryTree import BinaryTree

"""
"""
class BinarySearchTree( BinaryTree ):

  '''
  '''
  def __init__( self, v ):
    super( ).__init__( v )
  # end def

  '''
  '''
  def set_left( self, n ):
    if n is None:
      self.m_L = None
    else:
      if n.m_V < self.m_V and self.m_L is None:
        self.m_L = n
      # end if
    # end if
  # end def

  '''
  '''
  def set_right( self, n ):
    if n is None:
      self.m_R = None
    else:
      if self.m_V < n.m_V and self.m_R is None:
        self.m_R = n
      # end if
    # end if
  # end def

  '''
  '''
  def search( self, v ):
    if self.m_V < v:
      if not self.m_L is None:
        return self.m_L.search( v )
      else:
        return None
      # end if
    elif v < self.m_V:
      if not self.m_R is None:
        return self.m_R.search( v )
      else:
        return None
      # end if
    else:
      return self
    # end if
  # end def
# end class

## eof - $RCSfile$
