cmake_minimum_required (VERSION 3.0)
project(build-time-code-generation)

add_executable(test-runner main.cpp)
add_subdirectory(sample)
target_link_libraries(test-runner sample)
