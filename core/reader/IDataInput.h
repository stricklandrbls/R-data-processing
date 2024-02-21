#pragma once

class IDataInput {
public:
    virtual ~IDataInput() = default;
    virtual const char* get() noexcept = 0;
};