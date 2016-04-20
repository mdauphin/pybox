from icommand import icommand
import os
class Touch(icommand):
    def process(self,line):
        with open(line, 'a'):
            os.utime(line, None)
