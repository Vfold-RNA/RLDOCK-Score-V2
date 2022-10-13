set (BUILD_MODE MODE_NORMAL)

if(TEST_MODE)
  set (BUILD_MODE MODE_TEST)
endif(TEST_MODE)
if(PROFILE_MODE)
  set (BUILD_MODE MODE_PROFILE)
endif(PROFILE_MODE)
if(DEBUG_MODE)
  set (BUILD_MODE MODE_DEBUG)
endif(DEBUG_MODE)

cmake_minimum_required (VERSION 3.5)

project(RLDOCK-SCORE-V2)
# The version number.
set (VERSION_MAJOR 1)
set (VERSION_MINOR 0)
# configure a header file to pass some of the CMake settings to the source code
configure_file (
  ${PROJECT_SOURCE_DIR}/src/config.cmake.template
  ${PROJECT_SOURCE_DIR}/src/config.h
)

# set(BOOST_ROOT "${PROJECT_SOURCE_DIR}/lib/boost_1_71_0_installation")
# set(BOOST_INCLUDE "${BOOST_ROOT}/include")
# set(BOOST_LIB "${BOOST_ROOT}/lib")
set(LINKED_LIBS "-lstdc++fs" "-lpthread")
# message("${LINKED_LIBS}")

set(RL_SOURCE_INCLUDE "${PROJECT_SOURCE_DIR}/src")
set(RL_SOURCE_DIR "${PROJECT_SOURCE_DIR}/src")
include_directories("${RL_SOURCE_INCLUDE}")

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# collect all source files
# AUX_SOURCE_DIRECTORY(${RL_SOURCE_DIR} SOURCE_FILES)

set(RL_SRCS ${RL_SOURCE_DIR}/vec3d.cpp ${RL_SOURCE_DIR}/mol.cpp)
# set(RL_SRCS ${RL_SOURCE_DIR}/vec3d.cpp ${RL_SOURCE_DIR}/score.cpp)

set(RL_SOURCE_FILES ${RL_SOURCE_DIR}/main.cpp ${RL_SRCS})

# add the executable
# link library
if(${BUILD_MODE} STREQUAL "MODE_NORMAL")
set(CMAKE_CXX_FLAGS "-O3 -std=c++11 -static -static-libgcc -static-libstdc++")
add_executable(rldock_score_v2 ${RL_SOURCE_FILES})
target_link_libraries(rldock_score_v2 ${LINKED_LIBS})
endif()

if(${BUILD_MODE} STREQUAL "MODE_DEBUG")
set(CMAKE_CXX_FLAGS "-g -std=c++11 -static -static-libgcc -static-libstdc++")
add_executable(rldock_score_v2_debug ${RL_SOURCE_FILES})
target_link_libraries(rldock_score_v2_debug ${LINKED_LIBS})
endif()

if(${BUILD_MODE} STREQUAL "MODE_PROFILE")
set(CMAKE_CXX_FLAGS "-O3 -std=c++11")
add_executable(rldock_score_v2_profile ${RL_SOURCE_FILES})
target_link_libraries(rldock_score_v2_profile ${LINKED_LIBS} "-lprofiler")
endif()

if(${BUILD_MODE} STREQUAL "MODE_TEST")
set(CMAKE_CXX_FLAGS "-O3 -std=c++11 -static -static-libgcc -static-libstdc++")
add_executable(rldock_score_v2_test ${RL_SOURCE_FILES})
target_link_libraries(rldock_score_v2_test ${LINKED_LIBS})
endif()
