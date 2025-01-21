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

/**
 */
template< class _TId >
class SolveHanoi
{
public:
  using Self      = SolveHanoi;
  using TId       = _TId;
  using TMove     = std::tuple< TId, TId, TId >;
  using TSolution = std::vector< TMove >;

public:
  SolveHanoi( )
    {
    }
  virtual ~SolveHanoi( ) 
    {
    }

  void solve(
    const unsigned int& n, const TId& start, const TId& end, const TId& aux,
    bool init = true
    )
    {
      if( init )
        this->m_Solution.clear( );

      if( n > 0 )
      {
        if( n == 1 )
          this->m_Solution.push_back( std::make_tuple( start, end, aux ) );
        else
        {
          this->solve( n - 1, start, aux, end, false );
          this->solve( 1, start, end, aux, false );
          this->solve( n - 1, aux, end, start, false );
        } // end if
      } // end if
    }

public:
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
};

class hanoi_solver
{
  /* TODO
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
  */

  public static void main( String[] args )
    {
      /* TODO
         int n = 3;
         if( args.length > 0 )
         n = Integer.parseInt( args[ 0 ] );
         SolveHanoi( n, "tower 1", "tower 3", "tower 2" );
      */
    }
}

// eof - hanoi_solver.java
