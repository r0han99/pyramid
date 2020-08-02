# The pyramid utility

## Description
    The pyramid utility creates and visualises your ongoing or upcoming project directories like a stack structure where, your current most frequently used project directory paths(absolute) are pushed into the stack and then can be frequently changed into any of those directories for furthur work.The --set flag can be used to set the most prominently used absolute paths of the project directories, It has 3 modes to enter paths, a manual entry mode, in which user need to enter paths(comma-seperated), parse a path file with paths during run time or parse a file with paths pre-run time as --set [filename]. the file with paths should contain absolute paths of the directories that should be added to stack and should be structured one path per line.


## Usage

```bash
    # To set all the frequently visiting absolute paths.
    
    pyramid --set 
    
    # or 

    pyramid --help # for Manual

```

## Example

```bash
        
    pyramid --show-stack
```


### [E n d]