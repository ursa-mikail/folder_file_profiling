# Folder/File Profiling Python Script

This repository contains a Python script that demonstrates various OS and system functionalities for folder and file profiling. The script includes features for listing directories, walking through directories recursively, running system commands, changing directories, getting terminal size, listing environment variables, handling command line arguments, showing Python search paths, displaying Python interpreter information, and determining the size of objects in memory.

## Features

1. **Listing Directory Contents**
   - Function: `list_dir(path)`
   - Description: Lists the contents of a directory at one level.
   - Example Usage: `list_dir('.')`

2. **Recursively Listing Directory Contents**
   - Function: `walk_dir(path)`
   - Description: Recursively lists the contents of a directory.
   - Example Usage: `walk_dir('.')`

3. **Running System Commands**
   - Function: `run_system_command(command)`
   - Description: Runs a system command.
   - Example Usage: `run_system_command('echo Hello World')`

4. **Changing Working Directory**
   - Function: `change_directory(path)`
   - Description: Changes the current working directory.
   - Example Usage: `change_directory('..')`

5. **Getting Terminal Size**
   - Function: `get_terminal_size()`
   - Description: Prints the terminal size.
   - Example Usage: `get_terminal_size()`

6. **Listing Environment Variables**
   - Function: `list_environment_variables()`
   - Description: Lists all environment variables.
   - Example Usage: `list_environment_variables()`

7. **Handling Command Line Arguments**
   - Function: `show_sys_argv()`
   - Description: Shows command line arguments passed to the script.
   - Example Usage: `show_sys_argv()`

8. **Showing Python Search Paths**
   - Function: `show_sys_path()`
   - Description: Prints the Python module search paths.
   - Example Usage: `show_sys_path()`

9. **Displaying Python Interpreter Information**
   - Function: `show_sys_info()`
   - Description: Prints information about the Python interpreter.
   - Example Usage: `show_sys_info()`

10. **Determining Object Size in Memory And Other Profiles**
    - Function: `get_size(obj)` and `pretty_print_json(get_file_info(obj)`
    - Description: 
         - Displays the size of a specified object in bytes.
         - Gets the size of a file or directory in bytes.
         - Gets detailed information about a file or folder, including size, creation date, last modification date, and last access date.

