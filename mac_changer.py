#!/usr/bin/env python
import subprocess

subprocess.call("ifconfig eth0 down" ,shell=True)
subprocess.call("ifconfig eth0  hw ether 39:93:B7:46:36:A3 , shell=True)
subprocess.call("ifconfig eth0 up" , shell=True)
