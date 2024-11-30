import platform
import subprocess
import sys
import importlib
import json

def install_package(package):
    """Install the given package using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install package {package}: {e}")

def ensure_package(package_name):
    """Check if a package is installed, and install it if not."""
    try:
        importlib.import_module(package_name)
    except ImportError:
        print(f"Package {package_name} not found. Installing...")
        install_package(package_name)

# Ensure necessary packages are installed
ensure_package('psutil')
ensure_package('requests')
ensure_package('GPUtil')

import psutil
import requests
import GPUtil

def get_cpu_name():
    system = platform.system()
    if system == "Windows":
        return get_cpu_name_windows()
    elif system == "Linux":
        return get_cpu_name_linux()
    elif system == "Darwin":  # macOS
        return get_cpu_name_macos()
    else:
        return "Unsupported operating system"

def get_cpu_name_windows():
    try:
        output = subprocess.check_output("wmic cpu get name", shell=True)
        cpu_name = output.decode().split('\n')[1].strip()
        return cpu_name
    except Exception as e:
        return f"Error retrieving CPU name: {e}"

def get_cpu_name_linux():
    try:
        with open("/proc/cpuinfo") as f:
            for line in f:
                if line.startswith("model name"):
                    cpu_name = line.split(":")[1].strip()
                    return cpu_name
    except Exception as e:
        return f"Error retrieving CPU name: {e}"

def get_cpu_name_macos():
    try:
        output = subprocess.check_output("sysctl -n machdep.cpu.brand_string", shell=True)
        cpu_name = output.decode().strip()
        return cpu_name
    except Exception as e:
        return f"Error retrieving CPU name: {e}"

def get_system_info():
    system_info = {
        'os': platform.system(),
        'os_version': platform.version(),
        'architecture': platform.architecture()[0],
        'machine': platform.machine(),
        'processor': platform.processor(),
        'cpu_name': get_cpu_name()
    }

    # CPU information
    try:
        system_info['cpu_count'] = psutil.cpu_count(logical=False)
        system_info['cpu_count_logical'] = psutil.cpu_count(logical=True)
        system_info['cpu_freq'] = psutil.cpu_freq()._asdict()
    except Exception as e:
        system_info['cpu_info_error'] = str(e)

    # Memory (RAM) information
    try:
        virtual_memory = psutil.virtual_memory()._asdict()
        system_info['total_memory'] = virtual_memory['total']
        system_info['available_memory'] = virtual_memory['available']
        system_info['used_memory'] = virtual_memory['used']
        system_info['free_memory'] = virtual_memory['free']
        system_info['memory_percent_used'] = virtual_memory['percent']
    except Exception as e:
        system_info['memory_info_error'] = str(e)

    # Disk information
    try:
        disk_info = []
        for part in psutil.disk_partitions():
            usage = psutil.disk_usage(part.mountpoint)._asdict()
            disk_info.append({
                'device': part.device,
                'mountpoint': part.mountpoint,
                'fstype': part.fstype,
                'total': usage['total'],
                'used': usage['used'],
                'free': usage['free']
            })
        system_info['disk_info'] = disk_info
    except Exception as e:
        system_info['disk_info_error'] = str(e)

    # GPU information
    try:
        gpus = GPUtil.getGPUs()
        gpu_info = [{
            'id': gpu.id,
            'name': gpu.name,
            'load': gpu.load,
            'free_memory': gpu.memoryFree,
            'used_memory': gpu.memoryUsed,
            'total_memory': gpu.memoryTotal
        } for gpu in gpus]
        system_info['gpu_info'] = gpu_info
    except Exception as e:
        system_info['gpu_info_error'] = str(e)

    return system_info

def send_system_info(system_info):
    server_url = "https://yourserver.com/api/client_info"
    try:
        response = requests.post(server_url, json=system_info)
        if response.status_code == 200:
            print("System information sent successfully.")
        else:
            print(f"Failed to send information: {response.status_code}")
    except Exception as e:
        print(f"Failed to send information due to an error: {e}")

if __name__ == "__main__":
    try:
        info = get_system_info()
        print(json.dumps(info, indent=2))  # Print the collected system information
        send_system_info(info)  # Send the system information to the server
    except ImportError as e:
        print(f"Required module not installed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
