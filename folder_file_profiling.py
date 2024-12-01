import os
import sys
import time, json

def list_dir(path):
    try:
        items = os.listdir(path)
        print(f"Contents of '{path}': {items}")
    except Exception as e:
        print(f"Error listing directory contents: {e}")

def walk_dir(path):
    try:
        for root, dirs, files in os.walk(path):
            print(f"Root: {root}")
            print(f"Subfolders: {dirs}")
            print(f"Files: {files}")
            print()
    except Exception as e:
        print(f"Error walking directory: {e}")

def run_system_command(command):
    try:
        os.system(command)
    except Exception as e:
        print(f"Error running system command: {e}")

def change_directory(path):
    try:
        os.chdir(path)
        print(f"Changed directory to: {os.getcwd()}")
    except Exception as e:
        print(f"Error changing directory: {e}")

def get_terminal_size():
    try:
        size = os.get_terminal_size()
        print(f"Terminal size: Columns = {size.columns}, Rows = {size.lines}")
    except OSError:
        print("Error: Not running in a terminal, cannot get terminal size")

def list_environment_variables():
    try:
        env_vars = os.environ
        for key, value in env_vars.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Error listing environment variables: {e}")

def show_sys_argv():
    try:
        print(f"Command line arguments: {sys.argv}")
    except Exception as e:
        print(f"Error showing command line arguments: {e}")

def show_sys_path():
    try:
        print(f"Python search paths: {sys.path}")
    except Exception as e:
        print(f"Error showing Python search paths: {e}")

def show_sys_info():
    try:
        print(f"Python executable: {sys.executable}")
        print(f"Python version: {sys.version}")
        print(f"Python version info: {sys.version_info}")
        print(f"Platform: {sys.platform}")
    except Exception as e:
        print(f"Error showing Python info: {e}")

def show_sizeof_object(obj):
    try:
        size = sys.getsizeof(obj)
        print(f"Size of object {obj}: {size} bytes in description characters")
        print(f"Size of object {obj}: {get_size(obj)} bytes")
    except Exception as e:
        print(f"Error getting size of object: {e}")

def get_size(path):
    """Get the size of a file or folder.

    Args:
        path (str): The path to the file or folder.

    Returns:
        int: The size in bytes.
    """
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                total_size += os.path.getsize(file_path)
        return total_size
    else:
        raise ValueError(f"Path '{path}' is not a valid file or directory")

def get_file_info(path):
    """Get detailed information about a file or folder.

    Args:
        path (str): The path to the file or folder.

    Returns:
        dict: A dictionary containing detailed information.
    """
    if not os.path.exists(path):
        raise ValueError(f"Path '{path}' does not exist")

    info = {
        "path": path,
        "type": "Directory" if os.path.isdir(path) else "File",
        "size": get_size(path),
        "date_created": time.ctime(os.path.getctime(path)),
        "last_modified": time.ctime(os.path.getmtime(path)),
        "last_accessed": time.ctime(os.path.getatime(path))
    }
    
    return info

def pretty_print_json(data):
    """Pretty print a JSON object with an indent level of 4.

    Args:
        data (dict): The JSON data to print.
    """
    print(json.dumps(data, indent=4))

def print_demarcater():
    print(f"==========================================================")

if __name__ == "__main__":
    dir_start = os.getcwd()
    print(f"Starting directory: {dir_start}")

    dir_start = '/content/sample_data'
    os.chdir(dir_start)

    print(f"Changed directory to: {os.getcwd()}")

    print("1. os.listdir")
    list_dir(dir_start); print_demarcater()

    print("2. os.walk")
    walk_dir(dir_start); print_demarcater()

    print("3. os.system")
    run_system_command('echo Hello World'); print_demarcater()

    print("4. os.chdir")
    change_directory('..'); print_demarcater()

    print("5. os.get_terminal_size")
    get_terminal_size(); print_demarcater()

    print("6. os.environ")
    list_environment_variables(); print_demarcater()

    print("7. sys.argv")
    show_sys_argv(); print_demarcater()

    print("8. sys.path")
    show_sys_path(); print_demarcater()

    print("9. sys.executable, sys.version, sys.version_info & sys.platform")
    show_sys_info(); print_demarcater()

    print("10. sys_getsize and other profiles")
    file_path = '/content/sample_data/california_housing_test.csv'
    folder_path = '/content/sample_data/'

    data_target = file_path
    show_sizeof_object(data_target); print_demarcater()

    print(f"Size of the file '{file_path}': {get_size(file_path)} bytes")
    print(f"Size of the folder '{folder_path}': {get_size(folder_path)} bytes")

    print(f"Info of the file '{file_path}': "); pretty_print_json(get_file_info(file_path))
    print(f"Info of the folder '{folder_path}': "); pretty_print_json(get_file_info(folder_path))
    print_demarcater()

"""
Starting directory: /content
Changed directory to: /content/sample_data
1. os.listdir
Contents of '/content/sample_data': ['california_housing_test.csv', mnist_test.csv']
==========================================================
2. os.walk
Root: /content/sample_data
Subfolders: []
Files: [california_housing_test.csv', 'mnist_train_small.csv', 'mnist_test.csv']

==========================================================
3. os.system
==========================================================
4. os.chdir
Changed directory to: /content
==========================================================
5. os.get_terminal_size
Error: Not running in a terminal, cannot get terminal size
==========================================================
6. os.environ
SHELL: /bin/bash
:
USE_AUTH_EPHEM: 1
PYDEVD_USE_FRAME_EVAL: NO
==========================================================
7. sys.argv
Command line arguments: ['/usr/local/lib/python3.10/dist-packages/colab_kernel_launcher.py', '-f', '/root/.local/share/jupyter/runtime/kernel-ce3aaacf-0bbe-42da-87c3-39b90648d040.json']
==========================================================
8. sys.path
Python search paths: ['/content', '/env/python', '/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload', '', '/usr/local/lib/python3.10/dist-packages', '/usr/lib/python3/dist-packages', '/usr/local/lib/python3.10/dist-packages/IPython/extensions', '/usr/local/lib/python3.10/dist-packages/setuptools/_vendor', '/root/.ipython']
==========================================================
9. sys.executable, sys.version, sys.version_info & sys.platform
Python executable: /usr/bin/python3
Python version: 3.10.12 (main, Nov  6 2024, 20:22:13) [GCC 11.4.0]
Python version info: sys.version_info(major=3, minor=10, micro=12, releaselevel='final', serial=0)
Platform: linux
==========================================================
10. sys.getsizeof
Size of object /content/sample_data/california_housing_test.csv: 97 bytes in description characters
Size of object /content/sample_data/california_housing_test.csv: 301141 bytes
==========================================================
Size of the file '/content/sample_data/california_housing_test.csv': 301141 bytes
Size of the folder '/content/sample_data/': 56823553 bytes
Info of the file '/content/sample_data/california_housing_test.csv': 
{
    "path": "/content/sample_data/california_housing_test.csv",
    "type": "File",
    "size": 301141,
    "date_created": "Mon Nov 25 19:58:31 2024",
    "last_modified": "Mon Nov 25 19:13:23 2024",
    "last_accessed": "Mon Nov 25 19:13:23 2024"
}
Info of the folder '/content/sample_data/': 
{
    "path": "/content/sample_data/",
    "type": "Directory",
    "size": 56823553,
    "date_created": "Mon Nov 25 19:58:32 2024",
    "last_modified": "Mon Nov 25 19:13:24 2024",
    "last_accessed": "Mon Nov 25 19:58:32 2024"
}
==========================================================
"""