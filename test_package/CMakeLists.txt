# Quench warnings about CMP0003 with CMake 2.4.
if(COMMAND cmake_policy)
  cmake_policy(SET CMP0003 NEW)
endif(COMMAND cmake_policy)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

include_directories(
  ../src
)

add_executable(hayai_test
  ../sample/delivery_man_benchmark.cpp
  ../sample/delivery_man_benchmark_with_fixture.cpp
  ../sample/delivery_man_benchmark_parameterized.cpp
  ../sample/delivery_man_benchmark_parameterized_with_fixture.cpp
  ../sample/delivery_man_sleep.cpp
)

target_link_libraries(hayai_test
  hayai_main
  ${LIB_TIMING}
)
