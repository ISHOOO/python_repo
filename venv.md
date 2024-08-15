## Overview
A virtual environment in Python is an isolated environment that allows you to manage dependencies and packages for a specific project without affecting the global Python installation on your system. This is especially useful when working on multiple projects that might require different versions of libraries or Python itself.

## Benefits of Using a Virtual Environment
- **Isolate Dependencies** : Keeps your project’s dependencies separate from other projects and the system’s Python installation.
- **Avoid Conflicts** : Reduces the risk of version conflicts between packages used in different projects.
- **Reproducibility** : Helps to reproduce the exact environment your project needs, which is useful for others or future development.

- A virtual environment can be created in python using the following statement
`python -m venv <name of choice for virtual environment>` 

- The virtual environment can be activated by the following command:
`<name of environment>/Scripts/activated`

- Virtual environment files should never be pushed to a git repo because 
    a) they might cause the git repo to bloat the repo making it slower for push/pull operations
    b) they might cause other users to face problems regarding dependencies

## Execution policies in powershell
- Execution policies in PowerShell are a safety feature that determines the conditions under which PowerShell scripts can run. 
- They help prevent the accidental execution of potentially harmful scripts by setting rules on how scripts are executed. 
- Types of Execution policies:
    - **Restricted**: No scripts are allowed to run. This is the default setting on Windows client computers
    - **AllSigned**: Only scripts signed by a trusted publisher can run. This policy helps ensure that the scripts are from a known and trusted source.
    - **Bypass**: No restrictions at all. All scripts run regardless of their source or signature, and there are no warnings or prompts
    - **Unrestricted**: All scripts can run regardless of their source or signature. This policy offers the least protection and is typically used in environments where scripts need to be executed without restrictions.
    - **Undefined**: The execution policy is not set and inherits policy from the machine-level setting or defaults to the system's default if no machine-level setting exists.
    - **RemoteSigned**: Scripts created locally can run without a signature, but scripts downloaded from the internet must be signed by a trusted publisher. This is a common setting for development environments.

### Scope
The -Scope parameter specifies the scope of the policy change. The options are:

**Process**: Affects only the current PowerShell session.
**CurrentUser**: Affects only the current user.
**LocalMachine**: Affects all users on the computer.

- Example of a powershell command used to change excution policy. 
`Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope CurrentUser`
- Syntax: `Set-ExecutionPolicy <parameter> <type> <parameter> <type>`
