import tkinter as tk
import os
import subprocess
import threading

def execute_command(event=None):
    # Get the command from the Entry widget
    command = usercommand.get()
    usercommand.set("")

    command_output.config(state="normal")
    if command == "cls":
        command_output.delete(1.0, tk.END)
        command_output.config(state="disabled")
    elif command == "exit()" or command =="exit":
        root.quit()
    else:
        if command.startswith("cd "):
            # Extract the directory path from the command
            directory = command.split(" ", 1)[1]
            try:
                os.chdir(os.path.expanduser(directory))
                command_output.insert(tk.END, f">>> {command}\n")
                command_output.insert(tk.END, "\n \n")
                command_output.see(tk.END)
                command_output.config(state="disabled")
                return
            except FileNotFoundError:
                # Insert an error message into the output box if the directory doesn't exist
                command_output.insert(
                    tk.END, f"Error: Directory '{directory}' not found\n"
                )
                command_output.insert(tk.END, "\n \n")
                command_output.see(tk.END)
                command_output.config(state="disabled")
                return
          


        # Execute the command in a separate thread
        threading.Thread(target=run_command, args=(command,)).start()

def run_command(command):

     
    try:
        result = subprocess.run(
            ["cmd.exe", "/c", command], capture_output=True, text=True, check=True
        )

        # Check if the command executed successfully
        if isinstance(result, subprocess.CompletedProcess) and result.returncode == 0:
            command_output.config(state="normal")
            # Insert the command output into the output box
            command_output.insert(tk.END, f">>> {command}\n")
            command_output.insert(tk.END, result.stdout)
            command_output.insert(tk.END, "\n \n")
            command_output.see(tk.END)
            command_output.config(state="disabled")
        else:
            # Insert the error message into the output box
            command_output.config(state="normal")
            command_output.insert(tk.END, f">>> {command}\n")
            command_output.insert(tk.END, f"Error executing command: {result.stderr}\n")
            command_output.insert(tk.END, "\n \n")
            command_output.see(tk.END)
            command_output.config(state="disabled")
    except subprocess.CalledProcessError as e:
        # Insert the error message into the output box
        command_output.config(state="normal")
        command_output.insert(tk.END, f">>> {command}\n")
        command_output.insert(tk.END, f"Error executing command: {e.stderr}\n")
        command_output.insert(tk.END, "\n \n")
        command_output.see(tk.END)
        command_output.config(state="disabled")

# Set the default directory
os.chdir(os.path.expanduser("~"))

root = tk.Tk()
root.title("Windows Command Prompt Clone")
root.config(bg="black")
root.geometry("600x400")

usercommand = tk.StringVar()

commandlabel = tk.Label(text="Type Command and Press 'Enter' ", fg="white", bg="black")
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
    root, height=20, width=80, fg="white", bg="black", state="disabled", bd=0
)
command_output.pack()

root.mainloop()



