#include <gtest/gtest.h>

#include <reader/DataSet.h>
#include <fstream>
#include <iostream>
#include <filesystem>

struct CSVDataSetReader: public IDataSource {
public:
    std::filesystem::path path { "/home/orion/Code/data-processing/data/housing.csv" };   
    Headers headers() noexcept override {

    }
    // void read() noexcept override {
    //     std::ifstream csvFileStream { path };
    //     char buffer[1024];
    //     while(csvFileStream.good()){
    //         csvFileStream.getline(buffer, 1024);
    //         std::cout << "[line]: " << buffer << std::endl;
    //     }
    // }
    // void getHeaders(Headers *h) {
    //     std::ifstream csvFileStream { path };
    //     csvFileStream >> h;
    // }
};

struct TestableDataSource: public IDataSource {
public:
    Headers headers() noexcept override {
        Headers ret;
        ret.add("Sqft<I>")
            .add("bedrooms<I>")
            .add("bathrooms<I>")
            .add("price<D>");

        return ret;
    }
    void data() noexcept override {}
};

TEST(Init, init){
    TestableDataSource source;
    DataSet data { &source };

    for(const auto header : data.headers().keys())
        std::cout << "Header: " << header << std::endl;
}