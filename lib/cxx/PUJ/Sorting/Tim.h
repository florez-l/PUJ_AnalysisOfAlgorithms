// =========================================================================
// @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
// =========================================================================
#ifndef __PUJ__Sorting__Tim__h__
#define __PUJ__Sorting__Tim__h__

#include <PUJ/Sorting/Insertion.h>
#include <PUJ/Sorting/Merge.h>

namespace PUJ
{
  namespace Sorting
  {
    /**
     */
    template< class _TIt >
    void Tim( _TIt left, _TIt right, unsigned long long chunk_size = 32 )
    {
      unsigned long long N = std::distance( left, right );
      unsigned long long C = N / chunk_size;
      C += ( N % chunk_size != 0 )? 1: 0;

      // Sort chunks of chunk_size
      _TIt lIt = left, rIt;
      for( unsigned long long c = 0; c < C; ++c )
      {
        rIt = lIt;
        if( c < C - 1 ) std::advance( rIt, chunk_size );
        else            rIt = right;
        PUJ::Sorting::Insertion( lIt, rIt );
        lIt = rIt;
      } // end for
           
      // Merge chunks of size multiple of chunk_size
      _TIt mIt;
      for( unsigned long long s = chunk_size; s < N; s = s << 1 )
      {
        C = ( C / 2 ) + ( C % 2 );
        lIt = left;
        for( unsigned long long c = 0; c < C; ++c )
        {
          mIt = lIt;
          rIt = lIt;
          if( c < C - 1 )
          {
            std::advance( mIt, s );
            std::advance( rIt, s << 1 );
          }
          else
          {
            unsigned long long d = std::distance( lIt, right );
            std::advance( mIt, ( d < s )? d - 1: s );
            rIt = right;
          } // end if
          PUJ::Sorting::Merge( lIt, mIt, rIt );
          lIt = rIt;
        } // end for
      } // end while
    }
  } // end namespace
} // end namespace

#endif // __PUJ__Sorting__Tim__h__

// eof - Tim.h
