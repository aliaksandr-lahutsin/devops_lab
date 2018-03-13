import pip
import sys
import site
import subprocess


class AboutPythonEnvironment:
       
    def getSystemVersion(self):
        return sys.version
        
    def getVirtualEnvironment(self):
        result = subprocess.run(
            ['bash', '-c', 'pyenv virtualenvs'], 
            stdout=subprocess.PIPE)
        return result.stdout
    
    def getExecutableLocation(self):
        return sys.executable
    
    def getPipLocation(self):
        return site.getsitepackages()
    
    def getPythonPath(self):
        return sys.path

    def getInstalledPackages(self):
        installed_packages = pip.get_installed_distributions()
        installed_packages_list = sorted(
            ["%s==%s" % (i.key, i.version)
                for i in installed_packages])
    return installed_packages_list
    
    def getSitePackagesLocation(self):
        site_packages = next(p for p in sys.path if 'site-packages' in p)
        return site_packages
    
