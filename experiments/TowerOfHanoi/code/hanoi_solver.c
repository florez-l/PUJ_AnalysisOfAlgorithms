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

/*
 * Solve a Towers of Hanoi puzzle with n disks and start-aux-end towers.
 * @input n number of disks (natural).
 * @input (start,end,aux) identifications for each tower.
 * @output a sequence of movements <(from,to)> encoded with tower
 *         identificators.
 */
unsigned long SolveHanoi(
  unsigned char** M,
  unsigned int n, unsigned char start, unsigned char end, unsigned char aux
  )
{
  unsigned long nM = ( ( 2 << ( n - 1 ) ) - 1 ) << 1;

  *M = ( unsigned char* )calloc( nM, sizeof( unsigned char ) );

  return nM;

  /* TODO
     

     if( n == 1 )
     {
     if( nM == 0 )
     {
     printf( "first\n" );
     *M = ( unsigned char* )calloc( 2, sizeof( unsigned char ) );
     }
     else
     {
     printf( "second %d %d\n", nM, nM + 2 );
     *M = ( unsigned char* )reallocarray( M, nM + 2, sizeof( unsigned char ) );
     printf( "done\n" );
     }
     ( *M )[ nM ] = start;
     ( *M )[ nM + 1 ] = end;

     return nM + 2;
     }
     else
     {
     nnM = SolveHanoi( M, nM, n - 1, start, aux, end );
     nnM = SolveHanoi( M, nnM, 1, start, end, aux );
     nnM = SolveHanoi( M, nnM, n - 1, aux, end, start );
     return nnM;
     } end if
  */
}

/*
 * Print in an human readable way a sequence of Towers of Hanoi movements.
 * @input M a sequence of movements <(from,to)> encoded with tower
 *          identificators.
 */
void PrintHanoiSolution( unsigned char* M, unsigned long nM )
{
  unsigned long i;
  for( i = 0; i < nM; i += 2 )
    printf( "move from tower %d to tower %d\n", M[ i ], M[ i + 1 ] );
}

/*
 * *********************************************************************** *
 * ******************************** MAIN ********************************* *
 * *********************************************************************** *
 */
int main( int argc, char* argv[] )
{
  unsigned int n = 3;
  if( argc > 1 )
     n = atoi( argv[ 1 ] );
  if( n < 1 )
  {
    printf(
      "The puzzle is not defined with a non-natural number of disks.\n"
      );
    return 1;
  } /* end if */

  unsigned char* M = NULL;
  unsigned long nM = SolveHanoi( &M, n, 0, 1, 2 );
  PrintHanoiSolution( M, nM );
  return 0;
}

/* eof - hanoi_solver.c */
