import os
user_home = os.environ["PATH"]

print(user_home)
# os.environ["PYTHONPATH"] = "..."

import sys
sys.path.append("...")

import sys
sys.path.extend(["/path/to/dotpy/file/"])
