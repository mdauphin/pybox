from icommand import icommand
import os

class Cmd(icommand):
    def process(self,line):
        os.chdir(os.path.expandvars(line))
