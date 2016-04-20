from icommand import icommand
import argparse
import os
import shlex
import time
import stat
from pwd import getpwuid

class Ls(icommand):
    def process(self,line):
        parser = argparse.ArgumentParser(description='Argparse Test script')
        parser.add_argument("--all", '-a', action='store_true', help='do not ignore entries starting with .')
        parser.add_argument('-l', action='store_true', help='use a long listing format')
        params = shlex.split(line)
        args = parser.parse_args(params)
        files = os.listdir('.')
        if args.all:
            files = ['.', '..' ] + files
        if args.l:
            self.printlong(files)
        else:
            self.printshort(files)

    def printshort(self,files):
        print ' '.join(files)

    def permissions_to_unix_name(self,st):
        is_dir = 'd' if stat.S_ISDIR(st.st_mode) else '-'
        dic = {'7':'rwx', '6' :'rw-', '5' : 'r-x', '4':'r--', '0': '---'}
        perm = str(oct(st.st_mode)[-3:])
        return is_dir + ''.join(dic.get(x,x) for x in perm)

    def printlong(self,files):
        print "total %s" % 0
        for file in files:
            fstat = os.stat(file)
            right = self.permissions_to_unix_name(fstat)
            ntlink = fstat.st_nlink
            size = fstat.st_size
            owner = getpwuid(fstat.st_uid).pw_name
            group = getpwuid(fstat.st_gid).pw_name
            modification_time = time.ctime(os.path.getmtime(file))
            print "%s %5d %s %s %5d %s %s" % (right, ntlink, owner, group, size, modification_time, file )
