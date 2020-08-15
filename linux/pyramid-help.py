#!/opt/anaconda3/bin/python

print('\n\n')

# Manual

print('                       M A N U A L             ')

print('\n')

print('\033[1m' + 'NAME\n        pyramid' + '\033[0m'+'    -- create and contain current and anticipated project directory paths for frequent use.')

print('\n\n')

print('\033[1m' + 'SYNOPSIS' + '\033[0m' + '\n' + '         '+'\033[1m'+'pyramid'+'\033[0m'+'   --[option] ')

print('\n')

print('\033[1m' + 'DESCRIPTION' + '\033[0m' +'\n' + '         '+'\033[0m'+'The pyramid utility creates and visualises your ongoing or upcoming project directories like a stack structure where, your current most frequently used project directory paths(absolute) are pushed into the stack and then can be frequently changed into any of those directories for furthur work.The --set flag can be used to set the most prominently used absolute paths of the project directories, It has 3 modes to enter paths, a manual entry mode, in which user need to enter paths(comma-seperated), parse a path file with paths during run time or parse a file with paths pre-run time as --set [filename]. the file with paths should contain absolute paths of the directories that should be added to stack and should be structured one path per line.')

print('\n')

print('The following options available.')

print('\n')

print('         '+'\033[1m'+'--set [filename.txt]?'+'\033[0m'+'          sets the absolute-paths into the stack in bulk,either through a file with paths or during the run-time.')

print('\n')

print('         '+'\033[1m'+'--show | -s  [[--full-stack | -fstack] | [--simple | -simp]]'+'\033[0m'+'    Visualizes the stack with all the project directory paths by default, with --simple argument the stack output will be normalised.')

print('\n')

print('         '+'\033[1m'+'-cd | --chdir [Hex-id]'+'\033[0m'+'         Changes into the Absolute path which is poited by the HEAD, or simply changes to the top-element of the Project Stack. Theres is Catch for using this option, one must do ```source pyramid --push``` in order to change the directory,since sourcing the commmand will make the changes in the current shell or Provide a HEX-ID as an additional option to change to directory of that particular HEX-ID') 



print('\n')



print('         '+'\033[1m'+'--tree [Hex-id]'+'\033[0m'+'                invokes tree command to visualise the tree structure of the top[HEAD] project directory in the stack or if HEX-ID is provided the Tree structure of that absolute path is visualised.')

print('\n')

print('         '+'\033[1m'+'--open [Hex-id]'+'\033[0m'+'                Taking advantage of the MacOS ``open-command``, you can open the Directory GUI with this flag or with HEX-ID as a second flag you can open project-directory of that HEX-ID.')


print('\n')

print('         '+'\033[1m'+'--push'+'\033[0m'+'                         using ```pwd | xargs pyramid --push``` the absolute path of the current directory can be pushed into the project-stack.')


print('\n')

print('         '+'\033[1m'+'--pop'+'\033[0m'+'                          pops out the head directory path from the project-stack.')


print('\n')

print('         '+'\033[1m'+'--update'+'\033[0m'+'                       updates the stack-pointer [HEAD] to whatever the input given.')


print('\n')







print('\n\n'+'\033[1m'+'Improvise.Adapt.Overcome')

print('\n')

print('                                                3,Aug 2020.                                     ')

print('\n')

print('\033[1m'+'                                                  [E N D]                                         ')

print('\033[0m')
