import os
import tkinter as tk
import subprocess
import threading


def execute_command(event=None):
    # Get the command from the Entry widget
    command = usercommand.get()
    usercommand.set("")

    # Enable the output field temporarily to clear or display text
    command_output.config(state="normal")

    if command == "cls":
        # Clear the output field
        command_output.delete(1.0, tk.END)
    elif command == "exit()":
        # Exit the application
        root.quit()
    else:
        if command.startswith("cd "):
            # Change directory command
            directory = command.split(" ", 1)[1]
            try:
                os.chdir(os.path.expanduser(directory))
                # Display the command in the output field
                command_output.insert(tk.END, f">>> {command}\n")
                command_output.insert(tk.END, "\n \n")
                command_output.see(tk.END)
                # Disable the output field again
                command_output.config(state="disabled")
                return
            except FileNotFoundError:
                # Insert an error message if the directory doesn't exist
                command_output.insert(
                    tk.END, f"Error: Directory '{directory}' not found\n"
                )
                command_output.insert(tk.END, "\n \n")
                command_output.see(tk.END)
                command_output.config(state="disabled")
                return

        # Execute the command in a separate thread to avoid freezing the UI
        threading.Thread(target=run_command, args=(command,)).start()


def run_command(command):
    try:
        # Run the command using subprocess
        result = subprocess.run(
            ["cmd.exe", "/c", command], capture_output=True, text=True, check=True
        )

        # Enable the output field temporarily to display text
        command_output.config(state="normal")

        # Check if the command executed successfully
        if isinstance(result, subprocess.CompletedProcess) and result.returncode == 0:
            # Insert the command output into the output box
            command_output.insert(tk.END, f">>> {command}\n")
            command_output.insert(tk.END, result.stdout)
            command_output.insert(tk.END, "\n \n")
            command_output.see(tk.END)
        else:
            # Insert the error message into the output box
            command_output.insert(tk.END, f">>> {command}\n")
            command_output.insert(tk.END, f"Error executing command: {result.stderr}\n")
            command_output.insert(tk.END, "\n \n")
            command_output.see(tk.END)

        # Disable the output field again
        command_output.config(state="disabled")

    except subprocess.CalledProcessError as e:
        # Insert the error message into the output box
        command_output.insert(tk.END, f">>> {command}\n")
        command_output.insert(tk.END, f"Error executing command: {e.stderr}\n")
        command_output.insert(tk.END, "\n \n")
        command_output.see(tk.END)
        command_output.config(state="disabled")


# Set the default directory
os.chdir(os.path.expanduser("~"))

root = tk.Tk()
root.title("Windows Command Prompt Clone")
root.resizable(False, False)
root.config(bg="black")
root.geometry("600x400")

usercommand = tk.StringVar()

commandlabel = tk.Label(
    text="Type Command and Press 'Enter' ", fg="white", bg="black"
)
commandlabel.pack()
# Command entry widget
command_entry = tk.Entry(
    root,
    width=50,
    textvariable=usercommand,
    fg="white",
    bg="black",
    insertbackground="white",
)
command_entry.pack(pady=10)
command_entry.bind("<Return>", execute_command)

# Command output widget
command_output = tk.Text(
    root, height=20, width=80, fg="white", bg="black", state="disabled"
)
command_output.pack()

root.mainloop()
