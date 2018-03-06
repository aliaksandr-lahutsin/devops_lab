import psutil

class CpuAnalazer:
    #
    def _cpuIntervalTimeAnalyze(self):
        for x in range(1):
            return psutil.cpu_percent(interval = 5)
    #
    def _cpuIntervalTimePerCpuAnalyze(self):
        for x in range(1):
            return psutil.cpu_times_percent(interval = 5, percpu = False)
    #
    def _cpuCount(self):
        return psutil.cpu_count(self)
    #
    def _cpuCountLogical(self):
        return psutil.cpu_count(logical = False)
    #
    def _cpuStat(self):
        return psutil.cpu_stats()