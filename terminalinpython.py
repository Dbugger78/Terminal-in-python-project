import os
import subprocess

def terminal():
    print("==================================================")
    print("   Custom Hybrid Terminal (Python + OS Shell)   ")
    print("   Type 'exit' to quit.                           ")
    print("   Prefix with 'py-' to run Python code. for example: py- print(5+5)        ")
    print("==================================================")
    
    while True:
        try:
            # Get current working directory for the prompt
            cwd = os.getcwd()
            user_input = input(f"{cwd} > ").strip()
            
            # Handle exit
            if user_input.lower() == 'exit':
                print("Exiting terminal...")
                break
                
            if not user_input:
                continue
                
            # PATH 1: Execute Python Code ( checks for 'py-')
            if user_input.startswith("py-"):
                code = user_input[3:].strip()
                try:
                    # Using exec 
                    exec(code)
                except Exception as e:
                    print(f"Python Error: {e}")
                    
            # PATH 2: Execute Directory Changes (cd needs to happen in the main process)
            elif user_input.startswith("cd "):
                path = user_input[3:].strip()
                try:
                    os.chdir(path)
                except Exception as e:
                    print(f"Error changing directory: {e}")
                    
            # PATH 3: Execute Regular Terminal Commands
            else:
                # shell=True allows us to run built-in shell commands (dir, ls, echo, etc.)
                result = subprocess.run(user_input, shell=True, text=True)
                
        except KeyboardInterrupt:
           #If there is cntrl + c it closes it niclye
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"Unexpected error: {e}")
#Idk what thi does but stack overflow told me to do ot so I do it just saying this is the nly bit i got from stack overflow or any extrenal source
if __name__ == "__main__":
    terminal()