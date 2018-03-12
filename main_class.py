import json
import psutil
#
from pyenv_info_class import *

class MonitorPyEnvJson:
    #
    def outResultSetting(self):
        ape = AboutPythonEnvironment()
        try:
            data = {
                'version: ' : str(ape.getSystemVersion()).replace('\n', ''),
                'virtual_environments: ' : str(ape.getVirtualEnvironment()).replace('\\n', ''),
                'executable_location' : str(ape.getExecutableLocation()),
                'pip_location' : str(ape.getPipLocation()),
                'PYTHONPATH: ' : str(ape.getPythonPath()),
                'Installed Packages: ' : str(ape.getInstalledPackages()),
                'Site Packages Location: ' : str(ape.getSitePackagesLocation())
            }
            with open('data.json', 'w') as f:
                json.dump(data, f, indent = 4)
        except OSError:
                print ('error')
        return 0