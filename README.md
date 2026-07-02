# Terminal-in-python-project

A custom hybrid terminal built in Python. Its main use is creating a terminal on a computer where the temrinal may be inaccessible.

## How it works

It's a simple loop that reads what you type and decides what to do with it:

* If it starts with `py-`, it runs the rest as Python code.
* If it starts with `cd `, it changes directory.
* If it's `exit`, it quits.
* Anything else gets passed straight to the system shell to run as a normal command.

## Installation

* **Mac OS:**
```bash
brew update
brew install python@3.14
```

* **Linux:**
```bash
sudo apt update
sudo apt install python3.14
```

* **Windows:**
```powershell
winget install Python.Python.3.14
```

IF there are any problems or question please contact me at : doublexmas3d@gmail.com
