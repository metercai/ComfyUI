import subprocess
import sys

comfyd_path = "comfyd.py"
arguments = ["--preview-method auto", "--port 8188", "--disable-auto-launch"]
comfyd = subprocess.Popen([sys.executable, comfyd_path] + arguments)


