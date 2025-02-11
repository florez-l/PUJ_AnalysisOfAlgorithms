// =========================================================================
// @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
// =========================================================================
#ifndef __PUJ__Sorting__Quick__h__
#define __PUJ__Sorting__Quick__h__

#include <random>

namespace PUJ
{
  namespace Sorting
  {
    /**
     */
    template< class _TIt >
    _TIt Partition( _TIt left, _TIt right )
    {
      auto x = *right;
      /* TODO
         i = p - 1

         for j in range( p, r ):
         if S[ j ] <= x:
         i += 1
         S[ i ], S[ j ] = S[ j ], S[ i ]
         # end if
         # end for

         S[ i + 1 ], S[ r ] = S[ r ], S[ i + 1 ]
         return i + 1
      */
    }

    /**
     */
    template< class _TIt >
    _TIt RandomizedPartition( _TIt left, _TIt right )
    {
      std::mt19937 g;
      std::uniform_int_distribution< unsigned long long >
        d( 0, std::distance( left, right ) );
      auto i = left;
      std::advance( i, d( g ) );
      
      auto r = std::make_reverse_iterator( right );
      auto aux = *r;
      *r = *i;
      *i = aux;

      return( PUJ::Sorting::Partition( left, right ) );
    }

    /**
     */
    template< class _TIt >
    void Quick( _TIt left, _TIt right )
    {
      auto n = std::distance( left, right );
      if( n > 1 )
      {
        auto middle = PUJ::Sorting::RandomizedPartition( left, right );
        Quick( left, middle );
        Quick( middle, right );
      } // end if
    }
  } // end namespace
} // end namespace

#endif // __PUJ__Sorting__Quick__h__

// eof - $RCSfile$
