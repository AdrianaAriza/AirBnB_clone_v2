#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['35.229.28.179', '54.234.166.97']
env.user = "ubuntu"


def deploy():
    n_file = do_pack()
    if n_file is None:
        return False
    return do_deploy(n_file)


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        n1 = archive_path.split('/')
        n1 = n1[-1]
        n2 = n1.split('.')
        n3 = "/data/web_static/releases/{}".format(n2[0])
        run("mkdir -p {}".format(n3))
        run("tar -xzf /tmp/{} -C {}".format(n1, n3))
        run("rm /tmp/{}".format(n1))
        run("mv {}/web_static/* {}".format(n3, n3))
        run("rm -rf {}/web_static".format(n2))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(n3))
        return True
    except:
        return False


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
