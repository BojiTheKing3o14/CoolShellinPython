files = {}

recognized_commands = {
    'add': 2,
    'del': 1,
    'list': 0,
    'rename': 2,
    'rewrite': 2,
    'exit': 0,
    'open': 1
}


def execute_command(entered_command):
    if entered_command.startswith('/'):
        if len(entered_command) > 1:
            command = entered_command[1:].strip()

            # Split into function and input
            parts = command.split(maxsplit=1)
            func = parts[0]
            inp = parts[1] if len(parts) > 1 else ""

            # Split inp into at most 2 parts
            inp_parts = inp.split(maxsplit=1)
            inp1 = inp_parts[0] if len(inp_parts) > 0 else ""
            inp2 = inp_parts[1] if len(inp_parts) > 1 else ""

            # Count provided inputs
            number_of_inputs = 0
            if inp1:
                number_of_inputs += 1
            if inp2:
                number_of_inputs += 1

            if func in recognized_commands:
                needed_inputs = recognized_commands[func]
                if number_of_inputs == needed_inputs:
                    if func == 'add':
                        if inp1 in files:
                            return "Error: file already exists."
                        else:
                            files[inp1] = inp2
                            return f"File '{inp1}' added."
                    elif func == 'del':
                        if inp1 in files:
                            del files[inp1]
                            return f"File '{inp1}' deleted."
                        else:
                            return "Error: file not found."
                    elif func == 'list':
                        return "\n".join(files.keys()) if files else "No files found."

                    elif func == 'rename':
                        if inp1 in files:
                            if inp2 in files:
                                return "Error: new name already exists."
                            files[inp2] = files.pop(inp1)
                            return f"File '{inp1}' renamed to '{inp2}'."
                        else:
                            return "Error: file not found."
                    elif func == 'rewrite':
                        if inp1 in files:
                            files[inp1] = inp2
                            return f"File '{inp1}' rewritten."
                        else:
                            return "Error: file not found."
                    elif func == 'open':
                        if inp1 in files:
                            return f"{inp1}: {files[inp1]}"
                        else:
                            return "Error: file not found."
                    elif func == 'exit':
                        return "Exiting program..."  # You could integrate this into a loop control if needed
                else:
                    return f"Error: incorrect number of inputs.\nHelp: '{func}' requires {needed_inputs} input(s)."
            else:
                return f"Error: function not recognized.\nHelp: recognized commands are: {', '.join(recognized_commands.keys())}"
        else:
            return "Error: no command found.\nHelp: try typing something after '/'."
    else:
        return "Error: string not recognized as a command.\nHelp: try typing '/' at the start of your command."

while True:
    command = input("cmd > ")
    if command != "/exit":
        print(execute_command(command))
    else:
        print(execute_command(command))
        break
