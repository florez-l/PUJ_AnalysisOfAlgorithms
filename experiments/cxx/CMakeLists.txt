## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

include_directories(
  ${PROJECT_BINARY_DIR}/lib/cxx
  ${PROJECT_SOURCE_DIR}/lib/cxx
  )

add_executable(BubbleSort BubbleSort.cxx)
add_executable(InserionSort InsertionSort.cxx)
add_executable(MergeSort MergeSort.cxx)
add_executable(TimSort TimSort.cxx)

add_executable(LoopBubbleSort LoopBubbleSort.cxx)
add_executable(LoopInserionSort LoopInsertionSort.cxx)
add_executable(LoopMergeSort LoopMergeSort.cxx)
add_executable(LoopTimSort LoopTimSort.cxx)

## eof - $RCSfile$
