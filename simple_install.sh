#!/bin/bash
# 
# DO COMMANDS
yum install -y git gcc gcc-c++ make git patch openssl-devel zlib-devel readline-devel sqlite-devel bzip2-devel
#
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
#
# Set .bash_profile values
export PATH="/root/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
#
# Create soft-link
ln -s /root/.pyenv/bin/pyenv /bin
#
pyenv install 2.7
pyenv install 3.5.0
#
pyenv global 2.7
#
easy_install virtualenv
#
pyenv virtualenv py2.7
#
pyenv global 3.5.0
#
pyenv virtualenv py3.5
#
pyenv versions
