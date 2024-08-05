import platform

if platform.system() == 'Windows':
	import win32api as windows


def position():
    """ Find Out Mouse Position """
    return windows.GetCursorPos()
