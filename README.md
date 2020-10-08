# The pyramid utility

![pyramid0](https://user-images.githubusercontent.com/45916202/91566881-e61d4980-e961-11ea-8ad2-5800327af3bd.jpg)

```Artwork```


## Setup WorkFlow


![workflow3](https://user-images.githubusercontent.com/45916202/91566468-5b3c4f00-e961-11ea-95de-97a188ce47f2.jpg)




## Description

The **pyramid** utility creates  and visualises 
frequently used directories in the command-line, like a **stack-structure** where the most recurrently used directory of your choice will be at the top of the stack. You can now access this stack using the ```pyramid``` command with the coded optional flags and effiently change into the 
those directories without having to almost type the entire path everytime. 
This is one of the `n` other things that this utility can handle.


## Dependencies for Shell and Python3

```bash

    # Tree command ~ Linux
    sudo apt install tree 
    
    #and 
    
    # xdg-open utility ~ Linux
    sudo apt install xdg-open
   
    # MacOS
    brew install tree

    
    # Python dependencies ~ { Linux,MacOS }
    pip3 install -r requirements.txt


```
    
## Installation for Linux
```bash
   
   cd linux/
   
   ./setup.sh

```
    


## Usage

```bash
    # To set all the frequently visiting absolute paths.
    
    pyramid --set 
    
    # or 

    pyramid --help # for Manual

```

## Example

```bash
    pyramid s  
    
          #(or)
          
    pyramid f
```
<img width="690" alt="Screenshot 2020-08-28 at 6 44 42 PM" src="https://user-images.githubusercontent.com/45916202/91566648-9b033680-e961-11ea-8299-fded25ebdaf5.png">



*** 

_Sneak Peak into V1.0.2_ 

~ **Feature List**,

* Ability to interactively use inbuilt compression methods (gz,bz2) and packaging (zip) functionality.
* Ability to create Customised stacks to isolate content to that particular stack.
* New functionality flags ( del, truncate ).

~ **Code Efficiency Goals**,
* compatibility ++;
* Eliminating code redundancy.
* Vectorising ```--set``` function reducing Time Complexity


***
