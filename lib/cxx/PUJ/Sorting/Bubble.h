// =========================================================================
// @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
// =========================================================================
#ifndef __PUJ__Sorting__Bubble__h__
#define __PUJ__Sorting__Bubble__h__

namespace PUJ
{
  namespace Sorting
  {
    /**
     */
    template< class _TIt >
    void Bubble( _TIt left, _TIt right )
    {
      auto r_right = right;
      for( auto r_right = right; r_right != left; --r_right )
      {
        auto i = left;
        auto j = i;
        j++;
        for( ; j != r_right; ++i, ++j )
        {
          if( *i > *j )
          {
            auto x = *i;
            *i = *j;
            *j = x;
          } // end if
        } // end for
      } // end for
    }
  } // end namespace
} // end namespace

#endif // __PUJ__Sorting__Bubble__h__

// eof - $RCSfile$
