// =========================================================================
// @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
// =========================================================================
#ifndef __PUJ__Sorting__Helpers__h__
#define __PUJ__Sorting__Helpers__h__

namespace PUJ
{
  namespace Sorting
  {
    /**
     */
    template< class _TIt >
    bool is_sorted( _TIt left, _TIt right )
    {
      bool s = true;
      auto i = left;
      auto j = i;
      j++;
      for( ; j != right; ++i, ++j )
        s &= !( *j < *i );
      return( s );
    }
  } // end namespace
} // end namespace

#endif // __PUJ__Sorting__Helpers__h__

// eof - $RCSfile$
