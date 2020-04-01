AC_INIT(ADC_001_Py,0.0.0, [support@deepsoft.com], ADC_001_Py)
AC_CANONICAL_BUILD
AC_CANONICAL_HOST
AC_SUBST(build)
AC_CANONICAL_TARGET
AC_SUBST(target)
AC_CONFIG_SRCDIR(adc001py.i)
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

AC_CONFIG_FILES([Makefile])
