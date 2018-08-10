/usr/bin/python3.6
_author_ = "Mr.BlackPY"
#Showing Information Of System [sios Project]

import sys,os,datetime

print("Platform name:")
print(sys.platform)

print("os name:")
print(os.name)

print("os Path:")
print(os.getenv('PATH'))

print("current Path:")
print(os.getcwd())

print("current date & time:")
now = datetime.datetime.now()
print(now)

print("current user:")
print(os.getlogin())

print("default encoding:")
print(sys.getdefaultencoding())
