import psutil


class CpuAnalazer:

    def cpuIntervalTimeAnalyze(self):
        for x in range(1):
            return psutil.cpu_percent(interval=5)

    def cpuIntervalTimePerCpuAnalyze(self):
        for x in range(1):
            return psutil.cpu_times_percent(interval=5, percpu=False)

    def cpuCount(self):
        return psutil.cpu_count(self)

    def cpuCountLogical(self):
        return psutil.cpu_count(logical=False)

    def cpuStat(self):
        return psutil.cpu_stats()
