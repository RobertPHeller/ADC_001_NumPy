##-*- makefile -*-############################################################
#
#  System        : 
#  Module        : 
#  Object Name   : $RCSfile$
#  Revision      : $Revision$
#  Date          : $Date$
#  Author        : $Author$
#  Created By    : Robert Heller
#  Created       : Wed Apr 1 14:01:48 2020
#  Last Modified : <200401.1526>
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


pkgpruexedir = $(pkgpythondir)/pruexec

pkgpruexe_DATA = text0.bin text1.bin

DEVICE=am335x
PRU_CC_FLAGS = --silicon_version=3 -I. -I/usr/share/ti/cgt-pru/include/ -D$(DEVICE) -i/usr/share/ti/cgt-pru/lib
PRU_LINKER_SCRIPT = AM335x_PRU.cmd
PRU_INCLUDES = resource_table_empty.h pru_ctrl.h pru_intc.h pru_cfg.h pru_spi.h rsc_types.h pru_types.h

# PRU0 is the SPI stuff.
PRU0_SRCS = pru0.c pru_spi.c
PRU0_OBJS = pru0.obj pru_spi.obj
PRU0_MAP  = pru0.map
PRU0_EXES = data0.bin text0.bin

# PRU1 is the oscillator
PRU1_SRCS = pru1.c
PRU1_OBJS = pru1.obj
PRU1_MAP  = pru1.map
PRU1_EXES = data1.bin text1.bin

PRU_HEXPRU_SCRIPT = bin.cmd

EXTRA_DIST = $(PRU_INCLUDES) $(PRU0_SRCS) $(PRU1_SRCS) \
		$(PRU_HEXPRU_SCRIPT) $(PRU_LINKER_SCRIPT)

pru0.out: pru0.c pru_spi.c $(PRU_INCLUDES)
	$(PRU_CC) pru0.c pru_spi.c $(PRU_CC_FLAGS) -z $(PRU_LINKER_SCRIPT) -o $@ -m $(PRU0_MAP)
	

text0.bin data0.bin : pru0.out $(PRU_HEXPRU_SCRIPT)
	hexpru $(PRU_HEXPRU_SCRIPT) $<
	-mv text.bin text0.bin
	-mv data.bin data0.bin
	
pru1.out: pru1.c $(PRU_INCLUDES)
	$(PRU_CC) pru1.c $(PRU_CC_FLAGS) -z $(PRU_LINKER_SCRIPT) -o $@ -m $(PRU1_MAP)
                        
# Build PRU .bin file from ELF
text1.bin data1.bin: pru1.out $(PRU_HEXPRU_SCRIPT)
	hexpru $(PRU_HEXPRU_SCRIPT) $<
	-mv text.bin text1.bin
	-mv data.bin data1.bin
                                
