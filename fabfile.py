from fabric.api import local, run, env, cd


env.hosts = ['blog.moynibell.com']
env.user = 'chrisc'

def prepare_deploy():
    local("git add -p && git commit")


def push():
    local("git push origin master")


def deploy():
    code_dir = '/var/www/moyniblog/blog'
    with cd(code_dir):
        run("git pull")
        run("sudo service gunicorn restart")

        #/var/www/moyniblog/env/bin/gunicorn --workers 3 --bind 127.0.0.1:8099 --reload=True
