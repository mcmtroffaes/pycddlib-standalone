This package provides just the ``cdd`` module of pycddlib, without ``cddgmp``.
It can be compiled from the source distribution without needing cddlib or gmp installed,
and is suitable for installation of pycddlib on systems where cddlib and/or gmp
cannot be installed, such as for instance Google Colab.

Install from PyPI with::

    pip install pycddlib-standalone

Install from the source repository with::

    ./configure.py
    pip install .
