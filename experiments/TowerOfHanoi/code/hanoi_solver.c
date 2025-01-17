/* ====================================================================== */
/* @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)           */
/* ====================================================================== */
/* Compilation :                                                          */
/* gcc hanoi_solver.c -o hanoi_solver_c                                   */
/* ====================================================================== */
/* Usage :                                                                */
/* ./hanoi_solver_c [number of disks]                                     */
/* ====================================================================== */

#include <stdio.h>
#include <stdlib.h>

void SolveHanoi( unsigned int n, char* start, char* end, char* aux )
{
  if( n > 0 )
  {
    if( n == 1 )
      printf( "move top disk from %s to %s\n", start, end );
    else
    {
      SolveHanoi( n - 1, start, aux, end );
      SolveHanoi( 1, start, end, aux );
      SolveHanoi( n - 1, aux, end, start );
    } /* end if */
  } /* end if */
}

int main( int argc, char* argv[] )
{
  if( argc > 1 )
    SolveHanoi( atoi( argv[ 1 ] ), "tower 1", "tower 3", "tower 2" );
  else
    SolveHanoi( 3, "tower 1", "tower 3", "tower 2" );

  return 0;
}

/* eof - hanoi_solver.c */
