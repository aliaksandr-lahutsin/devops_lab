import psutil


class RamAnalazer:

    def virualMemoryUsage(self):
        return psutil.virtual_memory()

    def swapMemoryUsage(self):
        return psutil.swap_memory() 
