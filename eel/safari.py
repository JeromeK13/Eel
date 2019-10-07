import os
import subprocess as sps
import sys

# Every browser specific module must define run(), find_path() and name like this

name = 'Safari'


def run(path, options, start_urls):
    if options['app_mode']:
        for url in start_urls:
            sps.Popen([path, '--app=%s' % url] +
                      options['cmdline_args'],
                      stdout=sps.PIPE, stderr=sps.PIPE, stdin=sps.PIPE)
    else:
        args = options['cmdline_args'] + start_urls
        sps.Popen([path, '--new-window'] + args,
                  stdout=sps.PIPE, stderr=sys.stderr, stdin=sps.PIPE)


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
