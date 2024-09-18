This package provides just the ``cdd`` module of
[pycddlib](https://github.com/mcmtroffaes/pycddlib),
without ``cdd.gmp``.
It can be compiled from the source distribution
without needing cddlib and gmp installed,
and is suitable for installation of pycddlib on systems where cddlib and gmp
cannot be installed, such as for instance Google Colab.

* Download: https://pypi.org/project/pycddlib-standalone/#files

* Documentation: https://pycddlib.readthedocs.io/en/latest/

* Development: https://github.com/mcmtroffaes/pycddlib-standalone/

# Installation

From PyPI:

```shell
python -m pip install pycddlib-standalone
```

On Google Colab:

```
%pip install pycddlib-standalone
```

From source repository:

```shell
python configure.py
python -m pip install .
```
