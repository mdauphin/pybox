import cmd
import os
import imp
import inspect
import icommand

class ProxyCmd(object):
    def __init__(self,parent_class):
        self.parent_class = parent_class
    def process(self,line):
        ret = self.parent_class.process(line)
        if ret != None:
            print ret

class BoxCmd(cmd.Cmd):
    prompt = '$ '
    def do_exit(self, line):
        return True

def main():
    for mod in os.listdir('commands'):
        if mod.endswith('.py'):
            shortname = mod[:-3]
            module = imp.load_source( shortname, 'commands/%s' % mod)
            for cls in dir(module):
                attr=getattr(module,cls)
                if (inspect.isclass(attr)
                        and inspect.getmodule(attr)==module
                        and issubclass(attr,icommand.icommand)):
                    print "Load %s" % shortname
                    proxy = ProxyCmd(attr())
                    setattr(BoxCmd, 'do_%s'%shortname, proxy.process )
    BoxCmd().cmdloop()

if __name__ == '__main__':
    main()
