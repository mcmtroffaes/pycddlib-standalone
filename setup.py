"""Setup script for pycddlib-standalone."""

from setuptools import setup
from setuptools.extension import Extension
import sys

# pycddlib is a Python wrapper for Komei Fukuda's cddlib
# Copyright (c) 2008-2024, Matthias Troffaes
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

name = "cdd"
sources = [
  "pycddlib/cdd.pyx",
  "cddlib/lib-src/cddcore.c",
  "cddlib/lib-src/cddio.c",
  "cddlib/lib-src/cddlib.c",
  "cddlib/lib-src/cddlp.c",
  "cddlib/lib-src/cddmp.c",
  "cddlib/lib-src/cddproj.c",
  "cddlib/lib-src/setoper.c",
]
depends = [
    "include/cddlib/cdd.h",
    "include/cddlib/cddmp.h",
    "include/cddlib/cddtypes.h",
    "include/cddlib/setoper.h",
    "include/cddlib/splitmix64.h",
    "pycddlib/extern_cddlib.pxi",
    "pycddlib/extern_mytype.pxi",
    "pycddlib/extern_preamble.pxi",
]
undef_macros = ["GMPRATIONAL"]
extra_compile_args = ["-Iinclude/", "-Iinclude/cddlib/"] + ["/std:c11"] if (sys.platform == 'win32') else []

setup(
    ext_modules=[
        Extension(
            name=name,
            sources=sources,
            depends=depends,
            undef_macros=undef_macros,
            extra_compile_args=extra_compile_args,
        )
    ],
)
