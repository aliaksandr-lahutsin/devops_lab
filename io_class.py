import psutil

class IOAnalazer:
    #
    def _diskPartitionUsage(self):
        return psutil.disk_partitions()
    #
    def _diskUsageUsage(self):
        return psutil.disk_usage('/')  
    #
    def _diskIOCounters(self):
        return psutil.disk_io_counters(perdisk = True)    
    #
    def _netIOCounters(self):
        return psutil.net_io_counters(pernic = True)   
