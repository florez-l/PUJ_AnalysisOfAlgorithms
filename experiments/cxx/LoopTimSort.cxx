// =========================================================================
// @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
// =========================================================================

#include <chrono>
#include <iostream>
#include <iterator>
#include <random>
#include <vector>
#include <PUJ/Sorting/IsSorted.h>
#include <PUJ/Sorting/Tim.h>

int main( int argc, char** argv )
{
  unsigned int N = 1000;
  unsigned int S = 10;
  if( argc > 1 ) N = std::atoi( argv[ 1 ] );
  if( argc > 2 ) S = std::atoi( argv[ 2 ] );

  // Prepare some data: use same seed to get always same numbers
  std::vector< int > v( N );
  std::mt19937 gen( 0 );
  std::uniform_int_distribution< decltype( v )::value_type > d( -100, 100 );
  for( unsigned int n = 0; n < N; ++n )
    v[ n ] = d( gen );

  // Execute experiments
  for( unsigned int n = 0; n <= N; n += S )
  {
    decltype( v ) w( v.begin( ), v.begin( ) + n );
    auto s = std::chrono::steady_clock::now( );
    PUJ::Sorting::Tim( w.begin( ), w.end( ) );
    auto d = std::chrono::steady_clock::now( ) - s;
    auto t = std::chrono::duration_cast< std::chrono::nanoseconds >( d );

    std::cout << n << " " << t.count( ) << " " << std::endl;
  } // end for

  return( EXIT_SUCCESS );
}

// eof - LoopTimSort.cxx
