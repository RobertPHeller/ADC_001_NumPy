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
#  Last Modified : <200418.1451>
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



EXTRA_DIST = prussdrv.c pruss_intc_mapping.h \
		      spidriver_host.h adcdriver_host.c \
		      __prussdrv.h  adcdriver_host.h \
		      prussdrv.h spidriver_host.c \
		      adc001py.i __init__.py setup.py

pkgpyexec_SCRIPTS = __init__.py

BUILTEXT = build/lib.$(PYTHON_PLATFORM)-$(target_cpu)-$(PYTHON_VERSION)/_adc001py$(PYTHON_SO)
BUILTPKG = build/lib.$(PYTHON_PLATFORM)-$(target_cpu)-$(PYTHON_VERSION)/adc001py.py


$(BUILTEXT) $(BUILTPKG):	
	$(PYTHON) setup.py build

all: all-am $(BUILTEXT) $(BUILTPKG)
         

install-exec-hook: $(BUILTEXT) $(BUILTPKG)
	echo " $(MKDIR_P) '$(DESTDIR)$(pkgpyexecdir)'"
	$(MKDIR_P) "$(DESTDIR)$(pkgpyexecdir)"
	echo " $(INSTALL_PROGRAM) $(BUILTEXT) $(DESTDIR)$(pkgpyexecdir)/_adc001py$(PYTHON_SO)"
	$(INSTALL_PROGRAM) $(BUILTEXT) $(DESTDIR)$(pkgpyexecdir)/_adc001py$(PYTHON_SO) || exit 1;
	echo " $(INSTALL_SCRIPT) $(BUILTPKG) $(DESTDIR)$(pkgpyexecdir)/adc001py.py"
	$(INSTALL_SCRIPT) $(BUILTPKG) $(DESTDIR)$(pkgpyexecdir)/adc001py.py || exit 1

uninstall-hook:
	echo " rm -f $(DESTDIR)$(pkgpyexecdir)/_adc001py$(PYTHON_SO)"
	rm -f $(DESTDIR)$(pkgpyexecdir)/_adc001py$(PYTHON_SO)
	echo " rm -f $(DESTDIR)$(pkgpyexecdir)/adc001py.py
	rm -f $(DESTDIR)$(pkgpyexecdir)/adc001py.py

