import threading
import time
import queue
import logging
from config import app
from src.logger import log


class Block(threading.Thread):
    shared = False
    __instance__  = None
    
    def __init__(self):
        super().__init__()
        self.setup()
        log.debug('Thread initiated')
        
    def setup(self):
        pass
    
    def __new__(cls):
        if cls.shared == True:
            if cls.__instance__ == None:
                cls.__instance__ = object.__new__(cls)
            return cls.__instance__
            
        return object.__new__(cls)
        
        
    def setShared(self):
        self.shared = True
        
    def run(self):
        log.debug('Thread running')
        pass
    
    def stop(self):
        self._is_running = False
    


class IOBlock(Block):
    def __init__(self):
        super().__init__()
        self.daemon = False
    
    
    
class TaskBlock(Block):
    
    def __init__(self, inputQueue = None, outputQueue=None):
        if isinstance(inputQueue, queue.Queue):
            self.inQ = inputQueue
        else:
            self.inQ = queue.Queue()
            
            
            
        if isinstance(outputQueue, queue.Queue):
            self.outQ = outputQueue
        else:
            self.outQ = queue.Queue()
            
        
        super().__init__()
        self.daemon = True
        
    def addToQueue(self, value):
        log.debug('Add to queue: %s', value)
        self.inQ.put(value)
        
    def setOutput(self, value):
        
        self.outQ.put(value)
        
    def getOutput(self):
        return self.outQ.get()
    def setup(self):
        self.daemon = True
    