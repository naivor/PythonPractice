#!/bin/usr/env  python3
# -*- coding:utf-8 -*-

index=0

with open("/home/naivor/Workspace/Python/Dict.py",'r')  as f:
        for line in  f.readlines():
            print(line.strip())

            index+=1

            print("这是第 %d 行" % index )
with open("/home/naivor/Workspace/Python/Dict.py","w") as f:

    f.write("print('我是新添加的行，你在知道吗')")

    f.write("\n")
    f.write("print('什么，你居然不知道，我说我说新添加的行')")
    
    f.write("\n")
    f.write("print('记住了么？')")

    f.write("\n")
    f.write("print('哼，小样！')")
