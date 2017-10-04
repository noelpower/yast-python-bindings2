AC_INIT([yast], [1.0], [dmulder@suse.com])
AM_INIT_AUTOMAKE([-Wall -Werror foreign])

AC_CONFIG_MACRO_DIR([m4])
AM_PATH_PYTHON([2.7])
AX_PYTHON_DEVEL
AX_PKG_SWIG([], [], AC_MSG_ERROR([SWIG is required to build.]))
AX_SWIG_PYTHON
AM_PROG_AR
LT_INIT
AC_PROG_CXX

AC_CONFIG_FILES([
 Makefile
 src/Makefile
])
AC_OUTPUT
