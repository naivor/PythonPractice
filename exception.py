#!/usr/bin/env  python3
# -*- coding:utf-8 -*-

import logging


class FooError(ValueError):
    pass
    
def foo(s):
   n=int(s)
   if n==0:
        raise FooError("invalid value:%s" % s)
   else:
        return 10/n


def bar(s):
    return foo(s)*2

def main():

    try:
        bar("0")
    except FooError as e:
        logging.exception(e)
        print("捕获到一个FoorException")
    except Exception as e:
        logging.exception(e)


main()
print("END")
