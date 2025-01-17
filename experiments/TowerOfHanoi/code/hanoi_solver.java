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

class hanoi_solver
{
  public static void SolveHanoi( int n, String start, String end, String aux )
    {
      if( n > 0 )
      {
        if( n == 1 )
          System.out.println( "move top disk from " + start + " to " + end );
        else
        {
          SolveHanoi( n - 1, start, aux, end );
          SolveHanoi( 1, start, end, aux );
          SolveHanoi( n - 1, aux, end, start );
        } // end if
      } // end if
    }

  public static void main( String[] args )
    {
      int n = 3;
      if( args.length > 0 )
        n = Integer.parseInt( args[ 0 ] );
      SolveHanoi( n, "tower 1", "tower 3", "tower 2" );
    }
}

// eof - hanoi_solver.java
