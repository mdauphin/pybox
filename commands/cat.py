from icommand import icommand

class Cat(icommand):
    def process(self,line):
        with open(line) as f:
            return f.read()
