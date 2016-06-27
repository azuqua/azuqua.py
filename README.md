azuqua.py
=========

Python library for invoking Flos on Azuqua

## Install

```
python setup.py install
```

## Usage

```
import Azuqua

ACCESS_KEY = "foo"
ACCESS_SECRET = "bar"

azuqua = Azuqua.Azuqua(ACCESS_KEY, ACCESS_SECRET)

for flo in azuqua.flos():
  print "Invoke %s (%s) -> %r" % (flo.name, flo.alias, flo.invoke({ "foo": "bar" }))

```