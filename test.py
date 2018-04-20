from src.block import *
from config.app import *


class TestTask(TaskBlock):
    def run(self):
        while True:
            cmd = self.inQ.get()
            self.setOutput(cmd)
    
class TestIO(IOBlock):
    
    def run(self):
        while True:
            cmd = input(NAME)
            if cmd == 'x':
                break
            service = TestTask()
            service.start()
            service.addToQueue(cmd)
            print(service.getOutput())
                
 
ui = TestIO()       
ui.start()