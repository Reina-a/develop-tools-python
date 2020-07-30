import re

def is_abs_win_path(maybe_win_path: str) -> bool:

    # windows本地磁盘驱动器合法路径的正则表达式
    win_re = r'^([a-zA-Z]):\\([^\\/:*?"<>|\r\n]+\\?)*$'
    win_re_c = re.compile(win_re)
    if win_re_c.match(maybe_win_path):
        return True
    else:
        return False


def is_abs_linux_path(maybe_linux_path: str) -> bool:

    linux_re = r'^/([^/]+/)*[^/]+/?$'
    linux_re_c = re.compile(linux_re)
    if linux_re_c.match(maybe_linux_path):
        return True
    else:
        return False


def is_abs_wsl_share_path(maybe_wsl_share_path: str) -> bool:

    wsl_share_re =  r'^/mnt/([a-z])/([^/]+/)*[^/]+/?$'
    wsl_share_re_c = re.compile(wsl_share_re)
    if wsl_share_re_c.match(maybe_wsl_share_path):
        return True
    else:
        return False