import os
import subprocess as sps
import sys

# Every browser specific module must define run(), find_path() and name like this

name = 'Safari'


def run(_path, options, start_urls):
    for url in start_urls:
        cmd = 'open -a safari %s' % url
        sps.Popen(cmd, stdout=sys.stdout, stderr=sys.stderr, stdin=sps.PIPE, shell=True)


def find_path():
    if sys.platform == 'darwin':
        return _find_safari_mac()
    else:
        return None


def _find_safari_mac():
    default_dir = r'/Applications/Safari.app/Contents/MacOS/Safari'
    if os.path.exists(default_dir):
        return default_dir
    # use mdfind ci to locate Chrome in alternate locations and return the first one
    name = 'Safari.app'
    alternate_dirs = [x for x in sps.check_output(["mdfind", name]).decode().split('\n') if x.endswith(name)]
    if len(alternate_dirs):
        return alternate_dirs[0] + '/Contents/MacOS/Safari'
    return None
