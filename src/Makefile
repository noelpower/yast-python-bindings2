all:
	swig -c++ -I/usr/include/YaST2 -python yast-core.i
	g++ -fPIC yast-core_wrap.cxx -I/usr/include/python2.7 -I/usr/include/YaST2 -shared -L/usr/lib64/YaST2/plugin -lpy2UI -o _ycp.so

clean:
	rm yast-core_wrap.cxx ycp.py *.pyc ycp.so _ycp.so 2>/dev/null || echo
