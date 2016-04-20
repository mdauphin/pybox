from icommand import icommand
import os
class Rm(icommand):
    def process(self,line):
        os.remove(line)
        return ""
