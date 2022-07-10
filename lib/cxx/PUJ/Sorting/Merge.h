// =========================================================================
// @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
// =========================================================================
#ifndef __PUJ__Sorting__Merge__h__
#define __PUJ__Sorting__Merge__h__

#include <iterator>
#include <vector>

namespace PUJ
{
  namespace Sorting
  {
    /**
     */
    template< class _TIt >
    void Merge( _TIt left, _TIt middle, _TIt right )
    {
      using _TTraits = typename std::iterator_traits< _TIt >;
      using _TValue = typename _TTraits::value_type;

      std::vector< _TValue > l( left, middle ), r( middle, right );
      auto lIt = l.begin( );
      auto rIt = r.begin( );
      for( auto mIt = left; mIt != right; ++mIt )
      {
        if( lIt != l.end( ) && rIt != r.end( ) )
        {
          if( *lIt < *rIt )
          {
            *mIt = *lIt;
            lIt++;
          }
          else
          {
            *mIt = *rIt;
            rIt++;
          } // end if
        }
        else if( lIt != l.end( ) && rIt == r.end( ) )
        {
          *mIt = *lIt;
          lIt++;
        }
        else if( lIt == l.end( ) && rIt != r.end( ) )
        {
          *mIt = *rIt;
          rIt++;
        } // end if
      } // end for
    }

    /**
     */
    template< class _TIt >
    void Merge( _TIt left, _TIt right )
    {
      auto n = std::distance( left, right );
      if( n > 1 )
      {
        auto middle = left;
        std::advance( middle, n >> 1 );
        Merge( left, middle );
        Merge( middle, right );
        Merge( left, middle, right );
      } // end if
    }
  } // end namespace
} // end namespace

#endif // __PUJ__Sorting__Merge__h__

// eof - Merge.h
