#include <reader/DataSet.h>

DataSet::DataSet(IDataSource* source): _source{ source } {
    _headers = _source->headers();
}
