from abc import ABCMeta, abstractmethod

class icommand():
    __metaclass__ = ABCMeta

    @abstractmethod
    def process(self,line):
        pass
