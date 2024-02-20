add_executable(
    CSVReaderTest
    ./CSVReaderTest.cxx
)
# target_include_directories(
#     CSVReaderTest
#     PUBLIC ${CMAKE_SOURCE_DIR}/core
# )
target_link_libraries(
    CSVReaderTest
    dataprocessor
    GTest::gtest_main
)
gtest_discover_tests(CSVReaderTest)