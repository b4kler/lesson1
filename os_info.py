# нужно собрать информацию об операционной системе и версии python

# TODO запустить этот скрипт и закомитить резельтат его работы (файл os_info.txt)

import platform
import sys

info = 'OS info is \n{}\n\n Python version is {} {}'.format(platform.uname(), sys.version, platform.architecture())

print(info)
