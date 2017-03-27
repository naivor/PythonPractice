#!/usr/bin/env python3
# -*- coding:utf-8 -*-

print("first,let us use fork() to create a child process!")

import os

print("process %s start..." % os.getpid())

pid=os.fork()
if pid==0:
  print("I am child process %s and my parent is %s" % (os.getpid(),os.getppid()))
else:
  print("I %s just created a child process %s" % (os.getpid(),pid))



print("then , it's time  to create child process by using multiprocessing!")

from multiprocessing import Process

def run_proc(name):
    print("Run child process %s %s" % (name,os.getpid()))
    

if __name__=='__main__':
    print("Parent process %s" % os.getpid())

    p=Process(target=run_proc,args=("test",))

    print("Chile process will start")

    p.start()

    p.join()

    print("Child process end.")
