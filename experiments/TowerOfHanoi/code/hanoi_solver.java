/* =========================================================================
 * @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
 * =========================================================================
 * Compilation :
 * javac hanoi_solver.java
 * =========================================================================
 * Usage :
 * java hanoi_solver
 * =========================================================================
 */

import java.util.*;

class hanoi_solver
{
  /*
   * Solve a Towers of Hanoi puzzle with n disks and start-aux-end towers.
   * @input n number of disks (natural).
   * @input (start,end,aux) identifications for each tower.
   * @input {private} init a flag indicating that the puzzle has just started
   *        to be solved.
   * @output the sequence of movements <(from,to)> encoded with tower
   *         identificators is saved in the m_Solution attribute.
   */
  public static List< String > SolveHanoi(
    int n, String start, String end, String aux
    )
    {
      List< String > M = new ArrayList< String >( );
      SolveHanoi( n, start, end, aux, M );
      return M;
    }

  private static void SolveHanoi(
    int n, String start, String end, String aux, List< String > M
    )
    {
      if( n == 1 )
      {
        M.add( start );
        M.add( end );
      }
      else
      {
        SolveHanoi( n - 1, start, aux, end, M );
        SolveHanoi( 1, start, end, aux, M );
        SolveHanoi( n - 1, aux, end, start, M );
      } // end if
    }

  /*
   * Print in an human readable way a sequence of Towers of Hanoi movements.
   * @input M a sequence of movements <(from,to)> encoded with tower
   *          identificators.
   */
  public static void PrintHanoiSolution( List< String > M )
    {
      for( int i = 0 ; i < M.size( ); i += 2 )
        System.out.println(
          "move from " + M.get( i ) + " to " + M.get( i + 1 )
          );
    }

  /*
   * ********************************************************************* *
   * ******************************* MAIN ******************************** *
   * ********************************************************************* *
   */
  public static void main( String[] args )
    {
      int n = 3;
      if( args.length > 0 )
        n = Integer.parseInt( args[ 0 ] );
      if( n < 1 )
      {
        System.err.println(
          "The puzzle is not defined with a non-natural number of disks."
          );
        System.exit( 1 );
      } // end if

      List< String > M = SolveHanoi( n, "tower 1", "tower 3", "tower 2" );
      PrintHanoiSolution( M );
    }
}

// eof - hanoi_solver.java
