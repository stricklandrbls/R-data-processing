#include <gtest/gtest.h>

#include <reader/IReadDataSets.h>
#include <fstream>
#include <iostream>
#include <filesystem>
struct Headers {
    static constexpr size_t bufferLen { 2048 };
    char headerLineBuffer[bufferLen];
};
struct DataSet {
    std::string **headers;
};
struct CSVDataSetReader: public IReadDataSet {
public:
    std::filesystem::path path { "/home/orion/Code/data-processing/data/purchased.csv" };    
    void read() noexcept override {
        std::ifstream csvFileStream { path };
        char buffer[1024];
        while(csvFileStream.good()){
            csvFileStream.getline(buffer, 1024);
            std::cout << "[line]: " << buffer << std::endl;
        }
    }
    void getHeaders(Headers *h) {
        std::ifstream csvFileStream { path };
        csvFileStream.getline(h->headerLineBuffer, Headers::bufferLen);
        std::cout<<"Headers: "<< h->headerLineBuffer << std::endl;
    }
};

TEST(Init, init){
    CSVDataSetReader reader;
    Headers headers;
    reader.getHeaders(&headers);
}