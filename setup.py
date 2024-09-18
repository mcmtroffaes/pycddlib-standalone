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

sources = [
    "src/pycddlib/cython/_cdd.pyx",
    "src/cddlib/lib-src/cddcore.c",
    "src/cddlib/lib-src/cddio.c",
    "src/cddlib/lib-src/cddlib.c",
    "src/cddlib/lib-src/cddlp.c",
    "src/cddlib/lib-src/cddmp.c",
    "src/cddlib/lib-src/cddproj.c",
    "src/cddlib/lib-src/setoper.c",
]
depends = [
    "src/include/cddlib/cdd.h",
    "src/include/cddlib/cddmp.h",
    "src/include/cddlib/cddtypes.h",
    "src/include/cddlib/setoper.h",
    "src/include/cddlib/splitmix64.h",
    "src/pycddlib/cython/all.pxi",
    "src/pycddlib/cython/cdd.pxi",
    "src/pycddlib/cython/mytype.pxi",
    "src/pycddlib/cython/pycddlib.pxi",
    "src/pycddlib/cython/pyenums.pxi",
    "src/pycddlib/cython/setoper.pxi",
]
# #include "cdd.h" & #include "cddlib/cdd.h" both needed to compile
extra_compile_args = ["-Isrc/include/", "-Isrc/include/cddlib/"] + (
    ["/std:c11"] if (sys.platform == "win32") else []
)

setup(
    ext_modules=[
        Extension(
            name="cdd.__init__",
            sources=sources,
            depends=depends,
            extra_compile_args=extra_compile_args,
        ),
    ],
)
