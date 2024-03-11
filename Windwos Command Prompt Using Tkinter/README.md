# Windows Command Prompt Clone

This is a simple clone of the Windows Command Prompt built using Python built-in modules and Tkinter.

## How to Use 

1. Run the application using Python.
2. Enter commands in the entry field and press Enter to execute them.
3. The output of the commands will be displayed in the text area below.
4. To clear the output, type `cls` and press Enter.
5. To exit the application, type `exit()` and press Enter.


## Python Modules used 

- Threading Module

    The threading module is used to create and manage threads in Python. In our application, we use threading to execute commands asynchronously, allowing the user interface to remain responsive while commands are being executed in the background.

-  OS Module 

    The os module provides a portable way of using operating system-dependent functionality. In our application, we use the os module to interact with the file system, change directories, and handle environment variables.

- Subprocess Module 

    The subprocess module allows us to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. In our application, we use subprocess to execute shell commands (some commands cannot be executed in the cmd)and capture their output.


## Features

- Supports basic command execution , making and deleting files and directories , checking versions of programs (excluding 'python') , displaying content of files , etc.

## Limitations

- The application may freeze or become unresponsive while executing certain commands, especially those that require user input or have long execution times.

- Commands that require administrative privileges or access to system resources may not work properly.

- Python scripts or commands that open new windows or pop-up dialogs may not display correctly or may cause unexpected behavior.

- Some commands may not produce output or may not work as expected due to differences in environment variables or system configurations.

- The application does not support advanced features of the Windows Command Prompt, such as piping, redirection, or scripting.

