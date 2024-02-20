file(GLOB_RECURSE SRC_FILES "reader/*.h" "reader/*.cxx")
add_library(
    dataprocessor SHARED
    ./reader/DataSets.cxx
)
target_include_directories(
    dataprocessor
    PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}
)