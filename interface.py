import subprocess
import os
import time
import blessings


class Terminal_1:
    def __init__(self):
        self.term = blessings.Terminal()
        self.color = self.term.color(2)
        self.clear = self.term.clear
    def fullscreen(self):
        return self.term.fullscreen()
    
def custom_terminal(self):
    print("Type 'run' to start the server".upper())
    while True:
        command = input("$ ")        
        # command = "start server"
        if command == "run":
            print("Running...")
            time.sleep(1)            
            command = "python3 server.py"
            terminal_command = f'gnome-terminal -- bash -c "{command}; exec bash"'
            process = subprocess.Popen(terminal_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        elif command == "stop":
            print("Stopping...")
            time.sleep(1)
            command = "exit"
            terminal_command = f'gnome-terminal -- bash -c "{command}; exec bash"'
            process = subprocess.Popen(terminal_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        elif command == "chat":
            print("Opening chat...")
            time.sleep(1)
            command = "python3 client.py"
            # terminal_command = f'gnome-terminal -- bash -c "{command}; exec bash"'
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        else:
            ...

        output, error = process.communicate()

        if output:
            print("Output: ", output.decode())
        if error:
            print("Error: ", error.decode())
        time.sleep(1)


if __name__ == "__main__":
    term = Terminal_1()
    
    custom_terminal(term)