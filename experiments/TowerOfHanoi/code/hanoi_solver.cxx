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

void SolveHanoi(
  const unsigned int& n,
  const std::string& start,
  const std::string& end,
  const std::string& aux
  )
{
  if( n > 0 )
  {
    if( n == 1 )
      std::cout
        << "move top disk from " << start << " to " << end
        << std::endl;
    else
    {
      SolveHanoi( n - 1, start, aux, end );
      SolveHanoi( 1, start, end, aux );
      SolveHanoi( n - 1, aux, end, start );
    } // end if
  } // end if
}

int main( int argc, char** argv )
{
  unsigned int n = 3;
  if( argc > 1 )
    std::istringstream( argv[ 1 ] ) >> n;
  SolveHanoi( n, "tower 1", "tower 3", "tower 2" );

  return( EXIT_SUCCESS );
}

// eof - hanoi_solver.cxx
