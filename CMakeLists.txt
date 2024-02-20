cmake_minimum_required(VERSION 3.20)
project(data-processing)

set(CXX_STANDARD 20)
set(CXX_STANDARD_REQUIRED ON)

set(DATA_DIR ${CMAKE_SOURCE_DIR}/data)

add_subdirectory(core)

option(BUILD_TESTS "Build Test Executables" ON)

# Remove me in production env
set(BUILD_TESTS ON)

if (BUILD_TESTS)
    include(FetchContent)
    FetchContent_Declare(
        googletest
        URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
    )
    FetchContent_MakeAvailable(googletest)

    enable_testing()
    include(GoogleTest)

    add_subdirectory(tests)
endif()
