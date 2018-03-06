import psutil

class NetAnalazer:
    #    
    def _netConnectors(self):
        return psutil.net_connections()
    #
    def _netIfAddres(self):
        return psutil.net_if_addrs()  
    #
    def _netIfStats(self):
        return psutil.net_if_stats() 
