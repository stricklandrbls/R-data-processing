#pragma once
#include <vector>
#include <string>
#include <reader/IReadDataSets.h>


class DataSet {
public:
    DataSet(IDataSource* source);
    const Headers& headers() const noexcept { return _headers; }
protected:
    IDataSource *_source;
    Headers _headers;
};