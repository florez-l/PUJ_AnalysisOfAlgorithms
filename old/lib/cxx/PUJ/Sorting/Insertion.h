// =========================================================================
// @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
// =========================================================================
#ifndef __PUJ__Sorting__Insertion__h__
#define __PUJ__Sorting__Insertion__h__

#include <iterator>

namespace PUJ
{
  namespace Sorting
  {
    /**
     */
    template< class _TBIt >
    void Insertion( _TBIt left, _TBIt right )
    {
      if( std::distance( left, right ) < 2 )
        return;

      auto r_left = std::make_reverse_iterator( left );
      auto i = left;
      i++;
      for( ; i != right; ++i )
      {
        auto x = *i;
        auto j = std::make_reverse_iterator( i );
        auto k = j;
        k--;
        while( j != r_left && *j > x )
        {
          *k = *j;
          j++;
          k++;
        } // end while
        *k = x;
      } // end for
    }
  } // end namespace
} // end namespace

#endif // __PUJ__Sorting__Insertion__h__

// eof - $RCSfile$
