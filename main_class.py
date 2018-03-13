import json
import yaml
from pyenv_info_class import *


class MonitorPyEnvJson:
    
    def outResultSetting(self):
        ape = AboutPythonEnvironment()
        try:
            data = {
                'version: ': str(ape.getSystemVersion()).replace('\n', ''),
                'virtual_environments: ': str(
                    ape.getVirtualEnvironment()).replace('\\n', ''),
                'executable_location': str(ape.getExecutableLocation()),
                'pip_location': str(ape.getPipLocation()),
                'PYTHONPATH: ': str(ape.getPythonPath()),
                'Installed Packages: ': str(ape.getInstalledPackages()),
                'Site Packages Location: ': str(ape.getSitePackagesLocation())
            }

            data_yaml = dict(
                Version=str(ape.getSystemVersion()).replace('\n', ''),
                Virtual_environments=str(
                    ape.getVirtualEnvironment()).replace('\\n', ''),
                Executable_location=str(ape.getExecutableLocation()),
                Pip_location=str(ape.getPipLocation()),
                PYTHONPATH=str(ape.getPythonPath()),
                Packages=str(ape.getInstalledPackages()),
                Location=str(ape.getSitePackagesLocation())
            )

            with open('data.yml', 'w') as outfile: 
                yaml.dump(
                    data_yaml, 
                    outfile, 
                    default_flow_style=False)

            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)
        except OSError:
                print ('error')
        return 0
