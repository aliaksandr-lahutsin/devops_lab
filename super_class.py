import json
import psutil
#
from cpu_class import *
from ram_class import *
from io_class import *
from net_class import *

class MonitorJson:
    #
    def outResultSetting(self):
        ifs = CpuAnalazer()
        ims = RamAnalazer()
        ios = IOAnalazer()
        ins = NetAnalazer()
        data = {
            'count_cpu' : str(ifs.cpuCount()),
            'count_logical_cpu' : str(ifs.cpuCountLogical()),
            'virual_memory_usage' : str(ims.virualMemoryUsage()),
            'swap_memory_usage' : str(ims.swapMemoryUsage()),
            'disk_io_counters' : str(ios.diskIOCounters()),
            'network_if_stats' : str(ins.netIfStats())
        }
        with open('data.json', 'w') as f:
            json.dump(data, f)
        return 0
