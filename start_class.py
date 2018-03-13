from super_class import *
import json
from apscheduler.scheduler import Scheduler

sched = Scheduler()
sched.start()


def some_job():
    ifs = MonitorJson()
    ifs.outResultSetting()

data = json.load(open('config.json'))
sched.add_interval_job(some_job, seconds=data["interval"])
