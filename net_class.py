import psutil


class NetAnalazer:
   
    def netConnectors(self):
        return psutil.net_connections()

    def netIfAddres(self):
        return psutil.net_if_addrs()  

    def netIfStats(self):
        return psutil.net_if_stats() 
