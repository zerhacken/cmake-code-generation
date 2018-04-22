add_library(sample Sample.h ${CMAKE_CURRENT_BINARY_DIR}/Sample.cpp generate.py)

target_include_directories(sample PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}")
# Run at build time
add_custom_command(
    COMMAND python ${CMAKE_SOURCE_DIR}/sample/generate.py
    DEPENDS ${CMAKE_SOURCE_DIR}/sample/generate.py
    OUTPUT  ${CMAKE_CURRENT_BINARY_DIR}/Sample.cpp
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    COMMENT "Re-generating code for ${CMAKE_CURRENT_BINARY_DIR}/Sample.cpp"
)

# Run at configuration time
if (NOT EXISTS ${CMAKE_CURRENT_BINARY_DIR}/Sample.cpp)
    message("Generating ${CMAKE_CURRENT_BINARY_DIR}/Sample.cpp")
    execute_process(
        COMMAND python ${CMAKE_SOURCE_DIR}/sample/generate.py
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    )
endif()
