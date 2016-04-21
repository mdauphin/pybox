from icommand import icommand
import os
class Mv(icommand):
    def process(self,line):
        (src,dst) = line.split(' ')
        os.rename( src.strip(), dst.strip() )
