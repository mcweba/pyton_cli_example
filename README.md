# pyton_cli_example
Short demo for a CLI tool realized in python

## Project structure
Setup the project to have this structure

```
- cliExample 
    -- cliExample
        --- __init__.py
        --- __main__.py 
    -- install.sh
    -- setup.py
```
Let’s observe the files individually.

### __init__.py
The sole purpose of this file is to let _pip_ know that this is a package. To that end, an empty file will do for now.

### __main__.py
This file holds all the code. There can be multiple files, but since our tool is pretty simple and straightforward, we can dump it all inside a single file.

### setup.py
This file lets _pip_ know the details of the package such as name, version, and entry_points. Another important aspect it tackles is the dependency list indicated with _install_requires_ property; _pip_ will install all the packages in the list if they don’t exist on the user’s system.

### install.sh
This is a one-liner (_pip3 install -e ._) you could type into the Terminal manually too. Make sure you run _chmod +x install.sh_ first to give it executable rights. _-e_ lets pip know this is in development mode (so we do not have to keep installing and uninstalling after every change). _._ asks pip to install all the packages in the folder (which, if you recall, is only 1 anyway in our case)

## Installation using PIP
Run install.sh

## Use
After install you can run the example with

```
cliExample myArg1 myArg2
```
The output will be

```
param 1 was: myArg1 and param 2 was: myArg2
```
## Click Library
For input parameter usage the _click_ library was used. See [https://click.palletsprojects.com/en/5.x/](https://click.palletsprojects.com/en/5.x/)
