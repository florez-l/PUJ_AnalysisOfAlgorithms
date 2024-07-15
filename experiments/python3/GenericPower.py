## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import sys

'''
Compute the power operator between a real number a and a natural power b.
@input a A number that supports multiplication
@input b A a natural (positive integer or zero) number.
@output p = a.a.a.a.a... b times.
'''
def NaturalPower( a, b ):
  p = 1
  for i in range( b ):
    p *= a
  # end for
  return p
# end def

'''
Compute the power operator between a real number a and a real power b in
the real range [0, 1].
@input a A number that supports multiplication
@input b A a real number in the range [0, 1].
@output p = a**b
'''
def RationalPower( a, b ):
  return a ** b
# end def

'''
Compute the power operator between a real number a and a real power b.
@input a A number that supports multiplication
@input b A a real number
@output p = a**b
'''
def GenericPower( a, b ):
  d = abs( b - int( b ) )
  n = int( b - d )

  # Natural power
  np = 1
  if n < 0:
    np = 1.0 / NaturalPower( a, -n )
  elif n > 0:
    np = NaturalPower( a, n )
  # end if

  # Rational power
  rp = RationalPower( a, d )

  return np * rp
# end def

## -------------------------------------------------------------------------
## ------------------------------ MAIN SCRIPT ------------------------------
## -------------------------------------------------------------------------

a = 2
b = 0.5
if len( sys.argv ) > 1: a = float( sys.argv[ 1 ] )
if len( sys.argv ) > 2: b = float( sys.argv[ 2 ] )

print( 'Language solution =', a ** b )
print( '     Own solution =', GenericPower( a, b ) )

## eof - $RCSfile$
