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

// import SolveHanoi;

class hanoi_solver
{
  /**
   * Class that encapsulates a solver to the Towers of Hanoi puzzle.
   */
  public class SolveHanoi
  {
    /*
     * Create an object with an empty movements sequence.
     */
    public SolveHanoi( )
      {
      }

    /*
     * Solve a Towers of Hanoi puzzle with n disks and start-aux-end towers.
     * @input n number of disks (natural).
     * @input (start,end,aux) identifications for each tower.
     * @input {private} init a flag indicating that the puzzle has just started
     *        to be solved.
     * @output the sequence of movements <(from,to)> encoded with tower
     *         identificators is saved in the m_Solution attribute.
     */
    public void solve( int n, String start, String end, String aux )
      {
      }

    private void solve(
      int n, String start, String end, String aux, boolean init
      )
      {
        /* TODO
           if( init )
           this->m_Solution.clear( );

           if( n == 1 )
           this->m_Solution.push_back( std::make_tuple( start, end, aux ) );
           else
           {
           this->solve( n - 1, start, aux, end, false );
           this->solve( 1, start, end, aux, false );
           this->solve( n - 1, aux, end, start, false );
           } // end if
        */
      }

    // public:
    /*
     * Represent, in an human readable way, the sequence of Towers of Hanoi
     * movements saved in the attribute m_Solution.
     */
    /* TODO
       friend std::ostream& operator<<( std::ostream& out, const Self& solver )
       {
       for( unsigned long long i = 0; i < solver.m_Solution.size( ); ++i )
       {
       out
       << "from "
       << std::get< 0 >( solver.m_Solution[ i ] )
       << " to "
       << std::get< 1 >( solver.m_Solution[ i ] );
       if( i < solver.m_Solution.size( ) - 1 )
       out << std::endl;
       } // end for
       return( out );
    }

    private:
    TSolution m_Solution;
    */
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

      SolveHanoi solver = new SolveHanoi( );
      //solver.solve( n, "tower 1", "tower 3", "tower 2" );
    }
}

// eof - hanoi_solver.java
