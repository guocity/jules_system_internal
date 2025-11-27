import platform
import psutil
import subprocess
import sys
import shutil
import os
import socket
import urllib.request
import speedtest

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
    print("## System Information")
    uname = platform.uname()
    print(f"- **System**: {uname.system}")
    print(f"- **Node Name**: {uname.node}")
    print(f"- **Release**: {uname.release}")
    print(f"- **Version**: {uname.version}")
    print(f"- **Machine**: {uname.machine}")
    print(f"- **Processor**: {uname.processor}")
    print()

    # CPU info
    print("## CPU Info")
    print(f"- **Physical cores**: {psutil.cpu_count(logical=False)}")
    print(f"- **Total cores**: {psutil.cpu_count(logical=True)}")
    cpufreq = psutil.cpu_freq()
    if cpufreq:
        print(f"- **Max Frequency**: {cpufreq.max:.2f}Mhz")
        print(f"- **Min Frequency**: {cpufreq.min:.2f}Mhz")
        print(f"- **Current Frequency**: {cpufreq.current:.2f}Mhz")
    print()

    # Memory Info
    print("## Memory Info")
    svmem = psutil.virtual_memory()
    print(f"- **Total**: {get_size(svmem.total)}")
    print(f"- **Available**: {get_size(svmem.available)}")
    print(f"- **Used**: {get_size(svmem.used)}")
    print(f"- **Percentage**: {svmem.percent}%")
    print()

    # Disk Info
    print("## Disk Info")
    total, used, free = shutil.disk_usage("/")
    print(f"- **Total**: {get_size(total)}")
    print(f"- **Used**: {get_size(used)}")
    print(f"- **Free**: {get_size(free)}")
    print()

def get_network_info():
    print("## Network Information")

    if_addrs = psutil.net_if_addrs()
    if_stats = psutil.net_if_stats()

    for interface_name, interface_addresses in if_addrs.items():
        print(f"### Interface: `{interface_name}`")

        # Stats
        if interface_name in if_stats:
            stats = if_stats[interface_name]
            print(f"- **Status**: {'Up' if stats.isup else 'Down'}")
            print(f"- **Speed**: {stats.speed}Mbps")
            print(f"- **MTU**: {stats.mtu}")

        print("- **Addresses**:")
        for address in interface_addresses:
            if address.family == socket.AF_INET:
                print(f"  - **IPv4 Address**: {address.address}")
                print(f"  - **Netmask**: {address.netmask}")
                print(f"  - **Broadcast**: {address.broadcast}")
            elif address.family == socket.AF_INET6:
                print(f"  - **IPv6 Address**: {address.address}")
                print(f"  - **Netmask**: {address.netmask}")
                # IPv6 might not have broadcast
            elif address.family == psutil.AF_LINK: # AF_PACKET on Linux
                print(f"  - **MAC Address**: {address.address}")
                print(f"  - **Netmask**: {address.netmask}")
                print(f"  - **Broadcast**: {address.broadcast}")
        print()

    # IO Counters
    net_io = psutil.net_io_counters()
    print("### Global Network Stats")
    print(f"- **Total Bytes Sent**: {get_size(net_io.bytes_sent)}")
    print(f"- **Total Bytes Received**: {get_size(net_io.bytes_recv)}")
    print()

def get_wan_ip():
    print("### WAN IP Address")
    try:
        with urllib.request.urlopen('https://api.ipify.org') as response:
            ip = response.read().decode('utf-8')
            print(f"- **Public IP**: {ip}")
    except Exception as e:
        print(f"- **Public IP**: Error fetching IP ({e})")
    print()

def get_internet_speed():
    print("### Internet Speed Test")
    print("*Running speed test... (this may take a moment)*")
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download()
        upload_speed = st.upload()

        print(f"- **Download Speed**: {get_size(download_speed, suffix='bit/s')}")
        print(f"- **Upload Speed**: {get_size(upload_speed, suffix='bit/s')}")
    except Exception as e:
        print(f"- Error running speed test: {e}")
    print()

def get_python_env():
    print("## Python Environment")
    print(f"- **Python Version**: {sys.version}")
    print(f"- **Executable**: `{sys.executable}`")

    print("\n### Installed Packages")
    print("```")
    try:
        # Use subprocess to call pip list
        result = subprocess.run([sys.executable, '-m', 'pip', 'list'], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error getting pip packages: {e}")
    print("```")
    print()

def get_node_env():
    print("## Node Environment")

    # Check Node version
    try:
        node_version = subprocess.run(['node', '-v'], capture_output=True, text=True)
        if node_version.returncode == 0:
            print(f"- **Node Version**: {node_version.stdout.strip()}")
        else:
            print("- Node.js is not installed or not in PATH.")
    except FileNotFoundError:
        print("- Node.js is not installed or not in PATH.")

    # Check NPM version
    try:
        npm_version = subprocess.run(['npm', '-v'], capture_output=True, text=True)
        if npm_version.returncode == 0:
            print(f"- **NPM Version**: {npm_version.stdout.strip()}")

            print("\n### Global NPM Packages")
            print("```")
            npm_list = subprocess.run(['npm', 'list', '-g', '--depth=0'], capture_output=True, text=True)
            print(npm_list.stdout)
            print("```")
        else:
            print("- NPM is not installed or not in PATH.")
    except FileNotFoundError:
         print("- NPM is not installed or not in PATH.")
    print()

if __name__ == "__main__":
    print("# Machine Specifications and Environment\n")
    get_system_specs()
    get_network_info()
    get_wan_ip()
    get_internet_speed()
    get_python_env()
    get_node_env()
