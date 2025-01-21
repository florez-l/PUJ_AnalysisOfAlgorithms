/* =========================================================================
 * @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
 * =========================================================================
 * Compilation :
 * g++ -std=c++2a hanoi_solver.cxx -o hanoi_solver_cxx
 * =========================================================================
 * Usage :
 * ./hanoi_solver_cxx [number of disks]
 * =========================================================================
 */

#include <iostream>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>

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

// -------------------------------------------------------------------------
int main( int argc, char** argv )
{
  unsigned int n = 3;
  if( argc > 1 )
    std::istringstream( argv[ 1 ] ) >> n;

  SolveHanoi< std::string > solver;
  solver.solve( n, "tower 1", "tower 3", "tower 2" );
  std::cout << solver << std::endl;
  
  return( EXIT_SUCCESS );
}

// eof - hanoi_solver.cxx
