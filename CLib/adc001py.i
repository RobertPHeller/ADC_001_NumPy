/* -*- C -*- 
 *
 *  System        : 
 *  Module        : 
 *  Object Name   : $RCSfile$
 *  Revision      : $Revision$
 *  Date          : $Date$
 *  Author        : $Author$
 *  Created By    : Robert Heller
 *  Created       : Wed Apr 1 02:00:57 2020
 *  Last Modified : <200402.0926>
 *
 *  Description	
 *
 *  Notes
 *
 *  History
 *	
 *--------------------------------------------------------------
 *
 *    Copyright (C) 2020  Robert Heller D/B/A Deepwoods Software
 *			51 Locke Hill Road
 *			Wendell, MA 01379-9728
 *
 *    This program is free software; you can redistribute it and/or modify
 *    it under the terms of the GNU General Public License as published by
 *    the Free Software Foundation; either version 2 of the License, or
 *    (at your option) any later version.
 *
 *    This program is distributed in the hope that it will be useful,
 *    but WITHOUT ANY WARRANTY; without even the implied warranty of
 *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *    GNU General Public License for more details.
 *
 *    You should have received a copy of the GNU General Public License
 *    along with this program; if not, write to the Free Software
 *    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
 *
 * 
 *
 */

%define DOCSTRING
"This Python module provides a basic set of functions to access the 
ADC-001 BeagleBone Cape."
%enddef

%module(docstring=DOCSTRING) adc001py
%{
    static const char rcsid[] = "@(#) : $Id$";
#include "spidriver_host.h"
#include "adcdriver_host.h"
%}

%pythonbegin %{
import os
%}



%include typemaps.i


%feature("autodoc", "2") SampleRates;
%feature("docstring", "Allowed sample rates.
These are set by the AD7172 hardware. Consult the AD7172 datasheet for more info.") SampleRates;
enum SampleRates {
    SAMP_RATE_31250=5,
          SAMP_RATE_15625=6,
          SAMP_RATE_10417=7,
          SAMP_RATE_5208= 8,
          SAMP_RATE_2604= 9,
          SAMP_RATE_1008= 10,
          SAMP_RATE_504=  11,
          SAMP_RATE_400P6=12,
          SAMP_RATE_200P3=13,
          SAMP_RATE_100P2=14,
          SAMP_RATE_59P98=15,
          SAMP_RATE_50=   16};

// High level fcns which abstract away the need to know much about
// interfacing to the A/D.
/*void adc_config(void);*/

%feature("autodoc","adc_config(void) -> void") adc_config;
%feature("docstring", "Function to initialize the interface and get it ready to collect 
samples.") adc_config;
void adc_config(const char *pru_execpath);
%pythoncode %{
def adc_config() -> "void":
    libdir = os.path.dirname(__file__)
    #print(os.path.join(libdir,"pruexec"))
    _adc001py.adc_config(os.path.join(libdir,"pruexec"))
%} 

%feature("autodoc","2") adc_get_id_reg;
%feature("docstring", "Fetch the ID register.") adc_get_id_reg;
int adc_get_id_reg(void);
%feature("autodoc","2") adc_quit;
%feature("docstring", "Shutdown the module.") adc_quit;
void adc_quit(void);
%feature("autodoc","2") adc_reset;
%feature("docstring", "Reset the module.") adc_reset;
void adc_reset(void);
%feature("autodoc","2") adc_set_samplerate;
%feature("docstring", "Set the sample rate.") adc_set_samplerate;
/** Set the sample rate. 
 * @param rate The desired sample rate code.
 */
void adc_set_samplerate(int rate);
%feature("autodoc","2") adc_set_chan0;
%feature("docstring", "Select channel 0.") adc_set_chan0;
void adc_set_chan0(void);
%feature("autodoc","2") adc_set_chan1;
%feature("docstring", "Select channel 1.") adc_set_chan1;
void adc_set_chan1(void);


// Data acquisition fcns.
%feature("autodoc","2") adc_read_single;
%feature("docstring", "Fetch one sample.") adc_read_single;
float adc_read_single(void);

#include <pymem.h>

%typemap(in,numinputs=1) (uint32_t read_cnt, float *volts) {
    $1 = PyInt_AsLong($input);
    $2 = (float *) PyMem_Calloc($1,sizeof(float));
    
}

%typemap(argout) (uint32_t read_cnt, float *volts) {
    $result = PyList_New($1);
    for (int i=0;i < $1; i++) {
        PyList_SetItem($result, i, PyFloat_FromDouble($2[i]));
    }
    PyMem_Free($2);
}

%feature("autodoc","adc_read_multiple(read_cnt) -> list") adc_read_multiple;
%feature("docstring","Read up to 1024 samples.") adc_read_multiple;
void adc_read_multiple(int read_cnt, float *volts);

/** @} */
