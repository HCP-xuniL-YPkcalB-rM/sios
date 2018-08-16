#!/usr/bin/python3.6
_author_ = "Mr.BlackPY"
#Showing Information Of System [sios Project]
#GNU/LINUX

import sys,os,datetime

version = "0.2"

print("-----------------------------")

print("Platform name:")
print(sys.platform)

print("-----------------------------")

print("os name:")
print(os.name)

print("-----------------------------")

print("os Path:")
print(os.getenv('PATH'))

print("-----------------------------")

print("Shell:")
print(os.getenv('SHELL'))

print("-----------------------------")

print("Language and encoding:")
print(os.getenv('LC_NAME'))

print("-----------------------------")

print("SSH agent pid:")
print(os.getenv('SSH_AGENT_PID'))

print("-----------------------------")

print("current Path:")
print(os.getcwd())

print("-----------------------------")

print("current date & time:")
now = datetime.datetime.now()
print(now)

print("-----------------------------")

print("current user:")
print(os.getlogin())

print("-----------------------------")

print("Session manager:")
print(os.getenv('SESSION_MANAGER'))

print("-----------------------------")

print("Term:")
print(os.getenv('TERM'))

print("-----------------------------")

print("Text domain dir:")
print(os.getenv('TEXTDOMAINDIR'))

print("-----------------------------")

print("Home:")
print(os.getenv('HOME'))

print("-----------------------------")

#Creator: Mr.BlackPY
