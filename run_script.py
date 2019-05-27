#!/usr/bin/env python
import time
import os
from conf import ConfManagement
from core.defaultslog import *
from core.clearlogs import *
from core.statusDef import *
from core.statusCle import *


auto_path = ConfManagement().get_ini("automatedlogparsing")

date = time.strftime("%Y-%m-%d", time.localtime()).replace(' ', ':').replace(':', ':')
curpath = "/home/cle-test/%s" % date
os.makedirs(curpath, exist_ok=True)
os.system("cp 1.sh %s/"%auto_path)

def get_log_update(cmd, logs_patg):
    for i in range(2):
        os.system("{} > {}/{}.logs 2>&1 ".format(
            cmd, logs_patg, time.strftime( \
                "%Y-%m-%d-%H:%M:%S", \
                time.localtime()).replace(' ', ':'). \
                replace(':', ':'))
        )


path = os.path.join(curpath, "update")
os.makedirs(path, exist_ok=True)
make_path = auto_path +"/1.sh"
make_path += " make update"
print(make_path)
get_log_update(make_path, path)


def get_log_status(cmd, logs_patg):
    for i in range(2):
        os.system("{} > {}/{}.logs 2>&1 ".format(
            cmd, logs_patg, time.strftime( \
                "%Y-%m-%d-%H:%M:%S", \
                time.localtime()).replace(' ', ':'). \
                replace(':', ':'))
        )


path = os.path.join(curpath, "status")
os.makedirs(path, exist_ok=True)
make_path = auto_path +'/1.sh'
make_path += " make status"
get_log_status(make_path, path)



test_cmd = ["make httpd", "make nginx", "make memcached", "make redis", "make php", "make python", "make golang",
            "make node", "make openjdk", "make ruby"]


def get_log_test(cmd, logs_patg):
    for i in range(5):
        os.system("{} > {}/{}.logs 2>&1 ".format(
            cmd, logs_patg, time.strftime( \
                "%Y-%m-%d-%H:%M:%S", \
                time.localtime()).replace(' ', ':'). \
                replace(':', ':'))
        )

for i in test_cmd:
    path = os.path.join(curpath, "test_log")
    path = os.path.join(path, i.split(' ')[-1])
    os.makedirs(path, exist_ok=True)
    make_path = auto_path +'/1.sh'
    make_path += " %s"%i
    get_log_test(make_path, path)


sh = auto_path +'/1.sh'
os.system("rm %s"%sh)
