BUILT_SOURCES = ycp2.py
ycp2.py yast-core_wrap.cxx: yast-core.i
	$(SWIG) $(AX_SWIG_PYTHON_OPT) -c++ -I/usr/include/YaST2 -o $@ $<

python_PYTHON = ycp2.py yast.py

pyexec_LTLIBRARIES = _ycp2.la

_ycp2_la_SOURCES = yast-core_wrap.cxx yast-core.i

_ycp2_la_LDFLAGS = -module ${PYTHON_LDFLAGS}

_ycp2_la_LIBADD = -L/usr/lib64/YaST2/plugin -lpy2UI

_ycp2_la_CPPFLAGS = -I/usr/include/YaST2 ${PYTHON_CPPFLAGS}

CLEANFILES = ycp2.py yast-core_wrap.cxx
