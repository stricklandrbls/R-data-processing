#pragma once

class IReadDataSet {
public:
    ~IReadDataSet() = default;
    virtual void read() noexcept = 0;
};