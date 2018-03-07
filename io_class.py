import psutil

class IOAnalazer:
    #
    def diskPartitionUsage(self):
        return psutil.disk_partitions()
    #
    def diskUsageUsage(self):
        return psutil.disk_usage('/')  
    #
    def diskIOCounters(self):
        return psutil.disk_io_counters(perdisk = True)    
    #
    def netIOCounters(self):
        return psutil.net_io_counters(pernic = True)   
