##-*- makefile -*-############################################################
#
#  System        : 
#  Module        : 
#  Object Name   : $RCSfile$
#  Revision      : $Revision$
#  Date          : $Date$
#  Author        : $Author$
#  Created By    : Robert Heller
#  Created       : Wed Apr 1 14:01:35 2020
#  Last Modified : <200401.1748>
#
#  Description	
#
#  Notes
#
#  History
#	
#  $Log$
#
##############################################################################
#
#    Copyright (C) 2020  Robert Heller D/B/A Deepwoods Software
#			51 Locke Hill Road
#			Wendell, MA 01379-9728
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
# 
#
##############################################################################


pkgpyexec_LTLIBRARIES = adc001py.la
adc001py_la_SOURCES = prussdrv.c pruss_intc_mapping.h \
		      spidriver_host.h adcdriver_host.c \
		      __prussdrv.h  adcdriver_host.h \
		      prussdrv.h spidriver_host.c
nodist_adc001py_la_SOURCES = adc001py.c
adc001py_la_CFLAGS = $(PYTHON_CFLAGS) -I. -I../PRU
adc001py_la_LDFLAGS =  -g -module $(PYTHON_LDFLAGS)
adc001py_la_LIBADD = $(PYTHON_LIBS)

pkgpython_SCRIPTS = adc001py.py __init__.py

EXTRA_DIST = adc001py.i __init__.py

adc001py.c adc001py.py : adc001py.i
	$(SWIG) -python -py3 -builtin -o adc001py.c adc001py.i

install-pkgpyexecLTLIBRARIES: $(pkgpyexec_LTLIBRARIES)
	@$(NORMAL_INSTALL)
	echo " $(MKDIR_P) '$(DESTDIR)$(pkgpyexecdir)'"
	$(MKDIR_P) "$(DESTDIR)$(pkgpyexecdir)"
	echo " $(INSTALL) $(INSTALL_STRIP_FLAG) .libs/adc001py.so.0.0.0 $(DESTDIR)$(pkgpyexecdir)/_adc001py$(PYTHON_SO)"
	$(INSTALL) $(INSTALL_STRIP_FLAG) .libs/adc001py.so.0.0.0 $(DESTDIR)$(pkgpyexecdir)/_adc001py$(PYTHON_SO) || exit 1;


uninstall-pkgpyexecLTLIBRARIES:
	@$(NORMAL_UNINSTALL)
	echo " rm -f $(DESTDIR)$(pkgpyexecdir)/_adc001py$(PYTHON_SO)"
	rm -f $(DESTDIR)$(pkgpyexecdir)/_adc001py$(PYTHON_SO)


