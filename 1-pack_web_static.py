#!/usr/bin/python3
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """"""
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        date = datetime.now()
        format = "%Y%m%d%H%M%S"
        f_name = "versions/web_static_{}.tgz".format(date.strftime(format))
        local('tar -cvzf {} web_static'.format(f_name))
        return f_name
    except:
        return None
