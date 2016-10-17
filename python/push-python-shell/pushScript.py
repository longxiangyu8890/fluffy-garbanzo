#!/usr/bin/env python
# coding=utf-8
import os
import fnmatch
import codecs
import logging
import sys
import subprocess
from xml.etree import ElementTree
import sys   
from __builtin__ import list, str, filter
from apt.cache import Filter
from gtk._gtk import Item
from posix import chmod
from time import sleep
import xlwt
import random
import time

def remove_if_exist(filename):
    try:
        os.remove(filename)
    except OSError:
        print "this file",filename,"no exist"

if __name__ == '__main__':
    lib_paths_to_push = list()
    bin_paths_to_push = list()
    project_rootpath = None

    if len(sys.argv) <= 1:
        print "need to give project rootpath,or can not work"
        exit(-1)
    
    # get para
    if len (sys.argv) >= 2:
        cmd = -1  # ready to accept cmd
        for option in (sys.argv[1:]):#notice:  ***.py is argv[0]
            if cmd == -1:
                if option == "-p":  # the android root path 
                    cmd = 1
            else:
                if cmd == 1:
                    project_rootpath = option
                # ready for next cmd
                cmd = -1

    # 1.find "install" line in log file
    pipe = subprocess.Popen('grep -i install log', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    results = pipe.stdout.readlines()
    pipe.wait()

    for line in results:
	if line.startswith("Install:") and "system/lib" in line:
            tmp = line[len("Install:") :].strip() + "\n"
            #print "tmp:", tmp
            lib_paths_to_push.append(tmp)
	elif line.startswith("Install:") and "system/bin" in line:
            tmp = line[len("Install:") :].strip() + "\n"
            #print "tmp:", tmp
	    bin_paths_to_push.append(tmp)
            
    # 2.write paths to file
    file_name = "lib_paths_file"
    remove_if_exist(file_name)
    file_object = open('lib_paths_file', 'a')
    file_object.writelines(lib_paths_to_push)
    file_object.close()
            

    # 3.push paths to /system/lib or /system/bin
    print "here shell begin-- cur dir:", os.getcwd()
    pipe = subprocess.Popen('./pushShellV1 %s' % project_rootpath, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    results = pipe.stdout.readlines()
    pipe.wait()
    for result in results:
        print result
    print "here shell end--"
		

    


