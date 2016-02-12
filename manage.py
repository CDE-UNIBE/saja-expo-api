#!/usr/bin/env python
import sys
from os.path import join, dirname

import envdir

if __name__ == "__main__":
    envdir.read(join(dirname(__file__), 'envs'))

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
