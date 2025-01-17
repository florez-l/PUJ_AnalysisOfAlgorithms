## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

cmake_minimum_required(VERSION 3.0)
project(PUJ_AnalysisOfAlgorithms VERSION 1.0.0.1)

## == Output dirs
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR})

## == CMake directives and base applications
include(GenerateExportHeader)

## == Directories containing code
set(CMAKE_CXX_STANDARD 20)
subdirs(experiments/cxx)

## eof - $RCSfile$
