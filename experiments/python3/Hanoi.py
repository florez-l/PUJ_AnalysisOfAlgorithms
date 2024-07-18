## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import pprint, sys

'''
Compute the sequence of movements to solve a Hanoi towers game with n disks.
@input t_o Id of the origin tower
@input t_d Id of the destination tower
@input t_a Id of the auxiliary tower
@input n   A natural number representing the number of disks (n>0)
@output m: < m1, m2, ... > a sequence of movements, represented as a tuple of
        ids (origin,destination)
'''
def Hanoi( t_o, t_d, t_a, n ):
  if n == 1:
    return [ ( t_o, t_d ) ]
  else:
    m  = Hanoi( t_o, t_a, t_d, n - 1 )
    m += [ ( t_o, t_d ) ]
    m += Hanoi( t_a, t_d, t_o, n - 1 )
    return m
  # end if
# end def

## -------------------------------------------------------------------------
## ------------------------------ MAIN SCRIPT ------------------------------
## -------------------------------------------------------------------------

n = 3
if len( sys.argv ) > 1: n = int( sys.argv[ 1 ] )

print( '*************' )
print( '*** MOVES ***' )
print( '*************' )
pprint.pprint( Hanoi( 'origin', 'destination', 'auxiliary', n ) )

## eof - $RCSfile$
