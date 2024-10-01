## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import heapq
from BinaryTree import BinaryTree

"""
"""
class HuffmanTree( BinaryTree ):

  '''
  '''
  def __init__( self, f = 0, v = None ):
    super( ).__init__( ( f, v ) )
  # end def

  '''
  '''
  def __lt__( self, other ):
    return self.m_V[ 0 ] < other.m_V[ 0 ]
  # end def

  '''
  '''
  def encode( self ):
    if not self.m_V[ 1 ] is None:
      return { self.m_V[ 1 ]: '' }
    else:
      l = None
      r = None
      if not self.m_L is None and not self.m_R is None:
        l = self.m_L.encode( )
        r = self.m_R.encode( )
      elif self.m_L is None and not self.m_R is None:
        l = self.m_L.encode( )
      elif not self.m_L is None and self.m_R is None:
        r = self.m_R.encode( )
      # end if

      if not l is None:
        for t in l:
          l[ t ] = '0' + l[ t ]
        # end for
      # end if
      if not r is None:
        for t in r:
          r[ t ] = '1' + r[ t ]
        # end for
      # end if

      if not l is None and not r is None:
        return { **l, **r }
      elif l is None and not r is None:
        return l
      elif not l is None and r is None:
        return r
      else:
        return None
      # end if

    # end if
  # end def
x
  '''
  '''
  def decode( self, M, i = 0 ):
    if not self.m_V[ 1 ] is None:
      return ( self.m_V[ 1 ], i )
    else:
      if M[ i ] == '0':
        return self.m_L.decode( M, i + 1 )
      else:
        return self.m_R.decode( M, i + 1 )
      # end if
    # end if
  # end def
  
# end class

'''
'''
def build( T, P ):
  H = [ HuffmanTree( f, v ) for f, v in zip( P, T ) ]
  heapq.heapify( H )

  while len( H ) > 1:
    r = heapq.heappop( H )
    l = heapq.heappop( H )

    n = HuffmanTree( l.m_V[ 0 ] + r.m_V[ 0 ] )
    n.set_left( l )
    n.set_right( r )

    heapq.heappush( H, n )
  # end while

  return H[ 0 ]
# end def

'''
'''
def encode( hT, M ):
  code = hT.encode( )
  return ''.join( [ code[ t ] for t in M ] )
# end def

'''
'''
def decode( hT, eM ):
  dM = ''
  r = hT.decode( eM )
  while r[ 1 ] < len( eM ):
    dM += r[ 0 ] + ' '
    r = hT.decode( eM, r[ 1 ] )
  # end while
  dM += r[ 0 ]
  return dM
# end def

## eof - $RCSfile$
