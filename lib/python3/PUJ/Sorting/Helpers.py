## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

'''
Informs if a sequence is sorted
@input  S a sequence of comparable (<) elements
@output a boolean indicating whether S is sorted (True) or not (False)
'''
def is_sorted( S ):
  s = True
  i = 0
  while i < len( S ) - 1 and s:
    if S[ i + 1 ] < S[ i ]:
      s = False
    # end if
    i += 1
  # end for
  return s
# end def

## eof - $RCSfile$
