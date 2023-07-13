# child_to_execute_self.py

import os
import subprocess
import sys
from win32comext.shell import shell

if sys.argv[-1] != 'child':
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script]+sys.argv[1:]+['child'])
    shell.ShellExecuteEx(lpFile=sys.executable,lpParameters=params)
    sys.exit(0)

if sys.argv[-1] == 'child':
    os.system("notepad")
    sys.exit(0)
    