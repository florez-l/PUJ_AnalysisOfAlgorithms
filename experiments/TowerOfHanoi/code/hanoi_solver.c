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
void SolveHanoi_aux(
  unsigned char* M,
  unsigned int n, unsigned char start, unsigned char end, unsigned char aux,
  unsigned long* i
  )
{
  if( n == 1 )
  {
    M[ ( *i )++ ] = start;
    M[ ( *i )++ ] = end;
  }
  else
  {
    SolveHanoi_aux( M, n - 1, start, aux, end, i );
    SolveHanoi_aux( M, 1, start, end, aux, i );
    SolveHanoi_aux( M, n - 1, aux, end, start, i );
  } /* end if */
}

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

  unsigned long i = 0;
  SolveHanoi_aux( *M, n, start, end, aux, &i );

  return nM;
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
  unsigned long nM = SolveHanoi( &M, n, 1, 3, 2 );
  PrintHanoiSolution( M, nM );
  return 0;
}

/* eof - hanoi_solver.c */
