BUILT_SOURCES = ycp2.py
ycp2.py yast-core_wrap.cxx: yast-core.i $(libpy2UI)
	$(SWIG) $(AX_SWIG_PYTHON_OPT) -c++ -I/usr/include/YaST2 -o $@ $<

python_PYTHON = ycp2.py yast.py

pyexec_LTLIBRARIES = _ycp2.la libpy2lang_python.la

_ycp2_la_SOURCES = yast-core_wrap.cxx wrap.cpp yast-core.i

libpy2UIdir = /usr/lib64/YaST2/plugin

_ycp2_la_LDFLAGS = -module ${PYTHON_LDFLAGS} -Wl,-rpath=$(libpy2UIdir)

_ycp2_la_LIBADD = -L$(libpy2UIdir) -lpy2UI

_ycp2_la_CPPFLAGS = -std=c++11 -I/usr/include/YaST2 ${PYTHON_CPPFLAGS}


libpy2lang_python_la_SOURCES = Y2PythonClientComponent.cc Y2CCPythonClient.cc

#libpy2lang_python_la_LDFLAGS = -module ${PYTHON_LDFLAGS}
#libpy2lang_python_la_LDFLAGS = -module -lpython2.7 -lpthread -ldl -lutil -lm -Xlinker -export-dynamic
libpy2lang_python_la_LDFLAGS = -module -lpython2.7


#libpy2lang_python_la_LIBADD = -L$(builddir) -lpy2UI

libpy2lang_python_la_CPPFLAGS = -std=c++11 -I/usr/include/YaST2 ${PYTHON_CPPFLAGS}
#libpy2lang_python_la_CPPFLAGS = -std=c++11 -I/usr/include/YaST2 -I/usr/include/python2.7 -I/usr/include/python2.7 -fno-strict-aliasing -fmessage-length=0 -grecord-gcc-switches -O2 -Wall -D_FORTIFY_SOURCE=2 -fstack-protector -funwind-tables -fasynchronous-unwind-tables -g -DNDEBUG -fmessage-length=0 -grecord-gcc-switches -O2 -Wall -D_FORTIFY_SOURCE=2 -fstack-protector -funwind-tables -fasynchronous-unwind-tables -g -DOPENSSL_LOAD_CONF -fwrapv


CLEANFILES = ycp2.py yast-core_wrap.cxx
