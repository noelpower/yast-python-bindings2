#include "ytypes.h"

PyObject *ycp_to_pyval(YCPValue val)
{
    if (val->isString())
        return PyString_FromString(val->asString()->value().c_str());
    else if (val->isInteger())
        return PyInt_FromLong(val->asInteger()->value());
    else if (val->isBoolean())
        return PyBool_FromLong(val->asBoolean()->value());
    else if (val->isVoid() || val.isNull())
        Py_RETURN_NONE;
    else if (val->isFloat())
        return PyFloat_FromDouble(val->asFloat()->value());
    else if (val->isSymbol())
        return PyString_FromString(val->asSymbol()->symbol().c_str());
    else if (val->isPath())
        return PyString_FromString(val->asPath()->toString().c_str());
    else if (val->isList()) {
        PyObject* pItem;
        PyObject* pPythonTuple = PyTuple_New(val->asList()->size());
        for (int i = 0; i < val->asList()->size(); i++) {
            pItem = ycp_to_pyval(val->asList()->value(i));
            PyTuple_SetItem(pPythonTuple, i, pItem);
        }
        Py_INCREF(pPythonTuple);
        return pPythonTuple;
    } else if (val->isMap()) {
        PyObject* pKey;
        PyObject* pValue;
        PyObject* pPythonDict = PyDict_New();
        for (YCPMap::const_iterator it = val->asMap()->begin(); it != val->asMap()->end(); ++it) {
            pKey = ycp_to_pyval(it->first);
            pValue = ycp_to_pyval(it->second);
            if (pValue && pKey) {
                PyDict_SetItem(pPythonDict, pKey, pValue);
            }
        }
        Py_INCREF(pPythonDict);
        return pPythonDict;
    } else if (val->isTerm())
        return ycp_to_pyval(val->asTerm()->args());

    Py_RETURN_NONE;
}

