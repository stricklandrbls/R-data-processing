#pragma once
#include <list>
#include <variant>
#include <map>
#include <functional>
#include <vector>
#include <sstream>
#include <iostream>

class Headers {
public:
    using AllowedTypes = std::variant<int, double, std::string>;
    using DataTypeCast = std::function<AllowedTypes(const std::string&)>;

    Headers& add(const std::string& header) {
        std::string type = header.substr(header.find("<"));
        DataTypeCast castFn;
        if(type == "<I>") castFn = Headers::toInt;
        if(type == "<D>") castFn = Headers::toDouble;
        _headers[header] = castFn;
        return *this;
    }
    std::vector<std::string> keys() const noexcept {
        std::vector<std::string> ret;
        for(const auto key : _headers)
            ret.push_back(key.first);
        return ret;
    }
    auto count() noexcept { return _headers.size(); }
    static int toInt(std::string& str){
        int value;
        std::istringstream(str) >> value;
        return value;
    }
    static double toDouble(const std::string& str){
        double value;
        std::istringstream(str) >> value;
        return value;
    }
protected:
    std::map<std::string, DataTypeCast> _headers;
};

class IDataSource {
public:
    ~IDataSource() = default;
    virtual Headers headers() noexcept = 0;
    // virtual DataContent next() noexcept = 0;
    virtual void data() noexcept = 0;
};