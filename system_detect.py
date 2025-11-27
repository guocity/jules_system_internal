import platform
import psutil
import subprocess
import sys
import shutil
import os

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def get_system_specs():
    print("="*40, "System Information", "="*40)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")

    # CPU info
    print("="*40, "CPU Info", "="*40)
    print(f"Physical cores: {psutil.cpu_count(logical=False)}")
    print(f"Total cores: {psutil.cpu_count(logical=True)}")
    cpufreq = psutil.cpu_freq()
    if cpufreq:
        print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
        print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
        print(f"Current Frequency: {cpufreq.current:.2f}Mhz")

    # Memory Info
    print("="*40, "Memory Info", "="*40)
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")

    # Disk Info
    print("="*40, "Disk Info", "="*40)
    total, used, free = shutil.disk_usage("/")
    print(f"Total: {get_size(total)}")
    print(f"Used: {get_size(used)}")
    print(f"Free: {get_size(free)}")

def get_python_env():
    print("="*40, "Python Environment", "="*40)
    print(f"Python Version: {sys.version}")
    print(f"Executable: {sys.executable}")

    print("-" * 20)
    print("Installed Packages:")
    try:
        # Use subprocess to call pip list
        result = subprocess.run([sys.executable, '-m', 'pip', 'list'], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error getting pip packages: {e}")

def get_node_env():
    print("="*40, "Node Environment", "="*40)

    # Check Node version
    try:
        node_version = subprocess.run(['node', '-v'], capture_output=True, text=True)
        if node_version.returncode == 0:
            print(f"Node Version: {node_version.stdout.strip()}")
        else:
            print("Node.js is not installed or not in PATH.")
    except FileNotFoundError:
        print("Node.js is not installed or not in PATH.")

    # Check NPM version
    try:
        npm_version = subprocess.run(['npm', '-v'], capture_output=True, text=True)
        if npm_version.returncode == 0:
            print(f"NPM Version: {npm_version.stdout.strip()}")

            print("-" * 20)
            print("Global NPM Packages:")
            npm_list = subprocess.run(['npm', 'list', '-g', '--depth=0'], capture_output=True, text=True)
            print(npm_list.stdout)
        else:
            print("NPM is not installed or not in PATH.")
    except FileNotFoundError:
         print("NPM is not installed or not in PATH.")

if __name__ == "__main__":
    get_system_specs()
    get_python_env()
    get_node_env()
