import termios
import tty

import sys


orig_set = termios.tcgetattr(sys.stdin)


def restore_terminal_settings():
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_set)
