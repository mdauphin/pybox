from icommand import icommand
import os
class Echo(icommand):
    def process(self,line):
        return os.path.expandvars(line)
