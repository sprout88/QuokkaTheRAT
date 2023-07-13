import os
import subprocess
import sys

def run_subprocess():
    # Get the current script file path
    script_path = os.path.abspath(__file__)

    # Run the current script as a subprocess
    subprocess.Popen([sys.executable, script_path])

    # Exit the parent process
    sys.exit()

# Call the function to run the subprocess
run_subprocess()
print("hello")

# Rest of your code...
