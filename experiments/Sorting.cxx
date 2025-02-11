// =========================================================================
// @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
// =========================================================================

#include <algorithm>
#include <cctype>
#include <chrono>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

#include <PUJ/Sorting/Helpers.h>
#include <PUJ/Sorting/Bubble.h>
#include <PUJ/Sorting/Insertion.h>
#include <PUJ/Sorting/Merge.h>

using TValue = unsigned char;
using TSort = std::function< void( TValue*, TValue* ) >;

// -------------------------------------------------------------------------
void test_sort( const TValue* b, const TValue* e, TSort f )
{
  std::vector< TValue > L( b, e );

  auto s = std::chrono::steady_clock::now( );
  f( L.data( ), L.data( ) + L.size( ) );
  auto d = std::chrono::steady_clock::now( ) - s;
  if( !PUJ::Sorting::Helpers::is_sorted( L.begin( ), L.end( ) ) )
  {
    std::cerr
      << "Sequence was not ordered!: ** "
      << typeid( f ).name( )
      << " **" << std::endl;
    std::exit( EXIT_FAILURE );
  } // end if
  std::cout
    << std::setprecision( 4 ) << std::scientific
    <<
    std::chrono::duration_cast< std::chrono::nanoseconds >( d ).count( )
    *
    1e-9
    << " ";
}

// -------------------------------------------------------------------------
int main( int argc, char** argv )
{
  if( argc < 4 )
  {
    std::cerr
      << "  Usage: python " << argv[ 0 ]
      << " datafile size step"
      << " [permutation] [bubble] [insertion] [quick] [merge] [tim]"
      << std::endl;
    return( EXIT_FAILURE );
  } // end if
  std::string datafile = argv[ 1 ];
  unsigned long size, step;
  std::istringstream( argv[ 2 ] ) >> size;
  std::istringstream( argv[ 3 ] ) >> step;

  // Read some data
  std::ifstream datafile_ifs( datafile.c_str( ) );
  if( !datafile_ifs )
  {
    std::cerr << "Could not read input file." << std::endl;
    return( EXIT_FAILURE );
  } // end if
  datafile_ifs.seekg( 0, std::ios::end );
  std::size_t datafile_size = datafile_ifs.tellg( );
  datafile_ifs.seekg( 0, std::ios::beg );
  std::string datafile_buffer( size, 0 );
  datafile_ifs.read( &datafile_buffer[ 0 ], size );
  datafile_ifs.close( );
  const TValue* S
    = reinterpret_cast< const TValue* >( datafile_buffer.data( ) );
  unsigned long long S_size = datafile_size / sizeof( TValue );
  size = ( size < S_size )? size: S_size;

  // Get algorithms
  std::map< std::string, TSort > algorithms;
  algorithms[ "bubble" ] = PUJ::Sorting::Bubble< TValue* >;
  algorithms[ "insertion" ] = PUJ::Sorting::Insertion< TValue* >;
  algorithms[ "merge" ] = PUJ::Sorting::Merge< TValue* >;
  std::vector< std::string > A;
  for( int i = 4; i < argc; ++i )
  {
    std::string n = argv[ i ];
    std::transform(
      n.begin( ), n.end( ), n.begin( ),
      []( unsigned char c ) -> unsigned char
      {
        return( std::tolower( c ) );
      }
      );
    if( algorithms.find( n ) != algorithms.end( ) )
      A.push_back( n );
  } // end for

  std::cout << "size ";
  for( const auto& a: A )
    std::cout << a << " ";
  std::cout << std::endl;

  // Process data
  for( unsigned long long n = 0; n <= size; n += step )
  {
    std::cout << n << " ";
    for( const auto& a: A )
      test_sort( S, S + n, algorithms[ a ] );
    std::cout << std::endl;
  } // end for

  return( EXIT_SUCCESS );
}

// eof - Sorting.cxx
