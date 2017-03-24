#!/usr/bin/env  python3
# -*- coding:utf-8 -*-

from io  import StringIO

str = StringIO()
str.write("hello")
str.write(" ")
str.write("world!")

print(str.getvalue())


from io import BytesIO

byt=BytesIO()

byt.write("中国".encode("utf-8"))

print(byt.getvalue())
