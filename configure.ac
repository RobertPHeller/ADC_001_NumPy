AC_INIT(adc001py,0.0.0, [support@deepsoft.com], adc001py)
AC_CANONICAL_BUILD
AC_CANONICAL_HOST
AC_SUBST(build)
AC_CANONICAL_TARGET
AC_SUBST(target)
AC_CONFIG_SRCDIR(CLib/adc001py.i)
AM_INIT_AUTOMAKE
AC_CONFIG_MACRO_DIR([m4])
LT_INIT
if test "x${prefix}" = "xNONE"; then
    prefix=/usr/local
    fi
    if test "x${exec_prefix}" = "xNONE"; then
        exec_prefix="${prefix}"
        fi
        
BUILD_DIR=`pwd`
TOP_DIR=${BUILD_DIR}

AC_SUBST(TOP_DIR)
AC_SUBST(BUILD_DIR)

srcdir=`dirname $0`
cd $srcdir
SRC_DIR=`pwd`
cd $BUILD_DIR

AC_SUBST(SRC_DIR)

AC_SUBST(target)

AM_PATH_PYTHON([3.0])
PYTHONCONFIG="${PYTHON}-config"
AC_SUBST(PYTHONCONFIG)
PYTHON_CFLAGS="`$PYTHONCONFIG --cflags`"
PYTHON_INCLUDES="`$PYTHONCONFIG --includes`"
PYTHON_LIBS="`$PYTHONCONFIG --libs`"
PYTHON_LDFLAGS="`$PYTHONCONFIG --ldflags`"
PYTHON_SO="`$PYTHONCONFIG --extension-suffix`"
AC_SUBST(PYTHON_CFLAGS)
AC_SUBST(PYTHON_INCLUDES)
AC_SUBST(PYTHON_LIBS)
AC_SUBST(PYTHON_LDFLAGS)
AC_SUBST(PYTHON_SO)

AX_PKG_SWIG(1.3)

AC_PATH_PROG(PRU_CC,clpru)
AC_CONFIG_FILES([Makefile \
                 CLib/Makefile \
                 PRU/Makefile \
                 DeviceTree/Makefile])
AC_OUTPUT

