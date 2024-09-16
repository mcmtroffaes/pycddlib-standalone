This package provides just the ``cdd`` module of pycddlib, without ``cddgmp``.
It can be compiled from the source distribution without needing cddlib or gmp installed,
and is suitable for installation of pycddlib on systems where cddlib and/or gmp
cannot be installed, such as for instance Google Colab.

Install from PyPI with:

```shell
python -m pip install pycddlib-standalone
```

or, on Google Colab:

```
%pip install pycddlib-standalone
```

Install from the source repository with:

```shell
python configure.py
python -m pip install .
```
