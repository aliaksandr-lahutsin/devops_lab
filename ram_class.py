import psutil

class RamAnalazer:
    #
    def _virualMemoryUsage(self):
        return psutil.virtual_memory()
    #
    def _swapMemoryUsage(self):
        return psutil.swap_memory()  
