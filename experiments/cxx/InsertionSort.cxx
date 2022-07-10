// =========================================================================
// @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
// =========================================================================

#include <iostream>
#include <iterator>
#include <random>
#include <vector>
#include <PUJ/Sorting/IsSorted.h>
#include <PUJ/Sorting/Insertion.h>

// -------------------------------------------------------------------------
#define PUJ_print( _v )                                                 \
  std::copy(                                                            \
    _v.begin( ), _v.end( ),                                             \
    std::ostream_iterator< decltype( _v )::value_type >( std::cout, " " ) \
    );                                                                  \
  std::cout << std::endl

// -------------------------------------------------------------------------
int main( int argc, char** argv )
{
  unsigned int N = 10;
  if( argc > 1 )
    N = std::atoi( argv[ 1 ] );

  // Prepare some data
  std::vector< int > v( N );
  std::random_device dev;
  std::mt19937 gen( dev( ) );
  std::uniform_int_distribution< decltype( v )::value_type > d( -100, 100 );
  for( unsigned int n = 0; n < N; ++n )
    v[ n ] = d( gen );

  // Show initial data
  std::cout
    << "Given array is ("
    << PUJ::Sorting::IsSorted( v.begin( ), v.end( ) )
    << ")" << std::endl;
  PUJ_print( v );

  // Function Call
  PUJ::Sorting::Insertion( v.begin( ), v.end( ) );

  // Show results
  std::cout
    << "Sorted array is ("
    << PUJ::Sorting::IsSorted( v.begin( ), v.end( ) )
    << ")" << std::endl;
  PUJ_print( v );

  return( EXIT_SUCCESS );
}

// eof - InsertionSort.cxx
