
import os
import re
import csv
import sys
import pandas as pd
import numpy as np

content = [['alias','abs_path','priority']]

init_prior = 99

class color:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[1;32m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'




def __SHOW_STACK(showindexflag,msg='default'):

    with open('/usr/local/bin/projectstack.csv','r') as f:
        reader = csv.reader(f)
        headflag = 0
        next(reader)
        if(showindexflag):
            print()
            for index,row in enumerate(reader,0):
                if headflag == 0:
                    print('Index - '+str(index)+'  {}  '.format(row[1])+'(alias'+color.RED+'({})'.format(row[0])+color.END+')'+color.BOLD+color.RED+' <<< HEAD['+color.WARNING+msg+color.RED+color.BOLD+']'+color.END)
                    headflag+=1
                else:
                    print('Index - '+str(index)+'  {}  '.format(row[1])+'(alias'+color.RED+'({})'.format(row[0])+color.END+')')
        else:
            print()
            for row in reader:
                if headflag == 0:
                    print(color.RED+color.BOLD+'HEAD >>>'+color.END+' {}  '.format(row[1])+'(alias'+color.RED+'({})'.format(row[0])+color.END+')')
                    headflag+=1
                else:
                    print(color.WARNING+"                     |                        "+color.END)
                    print('        {}  '.format(row[1])+'(alias'+color.RED+'({})'.format(row[0])+color.END+')')

    print('\n')

def CHANGE_STACK():
    df = pd.read_csv('/usr/local/bin/projectstack.csv')

    if (np.unique(df['priority'][0] == 99)):
        print(color.GREEN+'Current Project Stack'+color.END)

        __SHOW_STACK(showindexflag=True)
        print()

        while True:
            changepri = input('Do you want to change the default HEAD pointer? '+color.GREEN+'{y/n}'+color.END+': ').lower()
            if(changepri == 'n'):
                __SHOW_STACK(False)
                break
            elif(changepri == 'y'):
                while True:
                    priorityinp = input('What project are you '+color.GREEN+'currently'+color.END+' working on? '+color.GREEN+'[index] : '+color.END)
                    if priorityinp.isdigit():
                        priorityinp = int(priorityinp)
                        if priorityinp in list(df.index):
                            df['priority'] = 0
                            df.at[priorityinp, 'priority']= 99
                            df = df.sort_values(by='priority',ascending=False)
                            df.to_csv('/usr/local/bin/projectstack.csv',index=False,encoding='utf-8')
                            break
                        else:
                            print(color.RED+'Invalid input,'+color.BOLD+' re-enter!'+color.END)
                            continue
                    else:
                        print(color.RED+'invalid index,'+color.BOLD+'re-enter'+color.END)
                        continue
                print()
                print('Stack updated!')
                print()
                __SHOW_STACK(showindexflag=False)
                break

            else:
                print('Invalid input,re-enter!')
                continue




try:
    if sys.argv[1] == '--set':
    
        if(os.stat('/usr/local/bin/projectstack.csv').st_size == 0):
            print('project stack is currently '+color.RED+'empty.'+color.END+'\nSetting a header. use'+color.GREEN+' --set flag or --help for assistance.'+color.END)

            with open('/usr/local/bin/projectstack.csv','w') as obj:
                writer = csv.writer(obj)
                writer.writerows(content)

        elif(os.stat('/usr/local/bin/projectstack.csv').st_size == 25 and len(sys.argv) == 2):
            print('creating a project stack.\n')
            print('There are no project paths present. invoking'+color.RED+' --push-recursive'+color.END)
            while True:
                SET_OPTION = input('Do you like to enter paths manually? <y/n>: ').lower()
                if(SET_OPTION == 'y'):

                    print('Enter your Absolute project paths manually [comma-separated]: ')
                    paths = list(input().split(','))
                    flag = 1
                    print()
                    for path in paths:

                        print(flag,path)

                        content.insert(flag,[path.split('/')[-1].strip(),path.strip(),init_prior])
                        init_prior = 0
                        flag+=1

                    with open('/usr/local/bin/projectstack.csv','w') as f:
                        writer = csv.writer(f)
                        writer.writerows(content)
                        print('Paths Set in the Stack')

                    print()
                    break



                elif(SET_OPTION == 'n'):
                    #color red

                    while True:
                        try:
                            pathsFile = input('\nEnter the '+color.GREEN+'path for the file'+color.END+' or '+color.BLUE+color.BOLD+'<?>'+color.END+' for assistance: ')
                            if (pathsFile != '?'):
                                with open(pathsFile,'r') as f:
                                    pathsread = f.readlines()
                                break
                            elif( pathsFile == '?'):
                                fileassist = color.WARNING+"""


    create a file with all the project paths you want to include
    in the project stack.
    open another terminal tab, navigate to each project directory and do
    """+color.GREEN+"""``` pwd >> pathfile.txt ```"""+color.END+color.WARNING+"""
    Then provide that pathfile to the input, you can either exit the code now with ctrl-c and
    providing the pathfile as an arugument '"""+color.GREEN+"""--set <pathfile.txt> """+color.WARNING+"""or during the run-time.

                                """+color.END
                                print(fileassist)


                        except FileNotFoundError:
                                print(color.RED+"File doesn't exist. "+color.BOLD+"[re-enter the path]"+color.END)
                                continue

                    print('['+color.GREEN+'Parsing file with paths.'+color.END+']')

                    flag = 1
                    for path in pathsread:

                        print(flag,path)
                        content.insert(flag,[path.split('/')[-1].strip(),path.strip(),init_prior])
                        init_prior=0
                        flag+=1

                    with open('/usr/local/bin/projectstack.csv','w') as f:
                        writer = csv.writer(f)
                        writer.writerows(content)
                        print('Paths Set in the Stack')
                        break


                else:
                    print('wrong input, enter <y/n>')
                    continue
                break

            print()
            print('presenting, the Stack')

            CHANGE_STACK()


        elif(os.stat('/usr/local/bin/projectstack.csv').st_size == 25 and len(sys.argv) == 3 ):

            print('['+color.GREEN+'Parsing file with paths.'+color.END+']')
            if( len(sys.argv) == 3):

                if (os.path.exists(sys.argv[2])):
                    pathsFile = sys.argv[2]
                    with open(pathsFile,'r') as f:
                        pathsread = f.readlines()
                    flag = 1
                    for path in pathsread:

                        print(flag,path)
                        content.insert(flag,[path.split('/')[-1].strip(),path.strip(),init_prior])
                        init_prior = 0
                        flag+=1

                    with open('/usr/local/bin/projectstack.csv','w') as f:
                        writer = csv.writer(f)
                        writer.writerows(content)
                        print('Paths Set in the Stack')

                    print()
                    print('presenting, the Stack')
                    CHANGE_STACK()

                else:
                    print('Parsed file ['+sys.argv[2]+'] Not found.')


        elif(len(sys.argv) > 3):
            #color red
            print('More than required args are provided, Try --help | -h for Assistance. [terminating]')

        else:
            print('Stack is already contained. do --show-stack to visualize')


    elif (sys.argv[1] == '--show-stack'):
        f = open('/usr/local/bin/projectstack.csv','r')
        lines = len(f.readlines())
        f.close()
        if lines > 1:

            __SHOW_STACK(False)
        else:
            print('project stack is '+color.RED+'empty.'+color.END+' do'+color.GREEN+' ```pwd | xargs pyramid --push``` '+color.END+'in you project directory.\n'+color.BLUE+'(or)'+color.GREEN+'\n--help | -h'+color.END+' for assistance.')

    elif (sys.argv[1] == '--update'):
        df = pd.read_csv('/usr/local/bin/projectstack.csv')


        if len(df) >= 2:

            if (np.unique(df['priority'][0] == 99)):
                print(color.GREEN+'Current Project Stack'+color.END)
                __SHOW_STACK(showindexflag=True,msg='current')
                while True:

                    priorityinp = input('What project are you '+color.GREEN+'currently'+color.END+' working on? '+color.GREEN+'[index] : '+color.END)
                    if priorityinp.isdigit():
                        priorityinp = int(priorityinp)
                        if priorityinp in list(df.index):
                            df['priority'] = 0
                            df.at[priorityinp, 'priority']= 99
                            df = df.sort_values(by='priority',ascending=False)
                            df.to_csv('/usr/local/bin/projectstack.csv',index=False,encoding='utf-8')
                            break
                        else:
                            print(color.RED+'invalid index,'+color.BOLD+'re-enter'+color.END)
                            continue
                    else:
                        print(color.RED+'Invalid its a character,'+color.BOLD+'enter an Index-number.'+color.END)
                print()
                print(color.GREEN+'Stack updated!'+color.END)
                print()
                __SHOW_STACK(showindexflag=False,msg='current')

            else:
                print(color.RED+'Theres something Wrong! [Terminating]'+color.END)
        else:
            print('project stack is '+color.RED+'empty.'+color.END+' do'+color.GREEN+' ```pwd | xargs pyramid --push``` '+color.END+'in you project directory.\n'+color.BLUE+'(or)'+color.GREEN+'\n--help | -h'+color.END+' for assistance.')


    elif (sys.argv[1] == '--pop'):

        f = open('/usr/local/bin/projectstack.csv','r')
        lines = len(f.readlines())
        f.close()

        if lines > 1:

            with open('/usr/local/bin/projectstack.csv','r') as f:
                    content = f.readlines()
                    LINES = len(content)

                    if (LINES != 2):
                        del content[1]
                        with open('/usr/local/bin/projectstack.csv','w') as f:
                            f.writelines(content)

                        df = pd.read_csv('/usr/local/bin/projectstack.csv')
                        df.at[0, 'priority']= 99
                        df.to_csv('/usr/local/bin/projectstack.csv',index=False, encoding='utf-8')

                        if (np.unique(df['priority'][0] == 99)):

                            print(color.GREEN+'Current Project Stack'+color.END)
                            __SHOW_STACK(showindexflag=True)
                            with open('/usr/local/bin/projectstack.csv','r') as f:

                                content = f.readlines()
                                LINES = len(content)

                            while True:
                                if(LINES != 2):

                                    defaultflag = input('Do you want to keep the default HEAD pointer?'+color.GREEN+' <y/n> : '+color.END)
                                    if (defaultflag == 'y'):
                                        break

                                    elif (defaultflag == 'n'):
                                        while True:
                                            priorityinp = input('What project are you '+color.GREEN+'currently'+color.END+' working on? '+color.GREEN+'[index] : '+color.END)
                                            if priorityinp.isdigit():
                                                priorityinp = int(priorityinp)
                                                if priorityinp in list(df.index):
                                                    df['priority'] = 0
                                                    df.at[priorityinp, 'priority']= 99
                                                    df = df.sort_values(by='priority',ascending=False)
                                                    df.to_csv('/usr/local/bin/projectstack.csv',index=False,encoding='utf-8')
                                                    break
                                                else:
                                                    print(color.RED+'Invalid index,'+color.BOLD+' re-enter!'+color.END)
                                                    continue
                                                break
                                            else:
                                                print(color.RED+'Invalid index,'+color.BOLD+'re-enter'+color.END)
                                                continue


                                        print()
                                        print(color.GREEN+'Stack updated!'+color.END)
                                        print()
                                        __SHOW_STACK(showindexflag=False)
                                        break

                                    else:
                                        print(color.RED+'Invalid input,'+color.BOLD+' re-enter!'+color.END)
                                        continue
                                else:
                                    print(color.GREEN+'Final Stack'+color.END)
                                    print()
                                    __SHOW_STACK(showindexflag=False)
                                    break


                        else:
                            print(color.RED+'Theres something Wrong! [Terminating]'+color.END)


                    else:
                        print(color.RED+'\n->Theres only '+color.BOLD+'one'+color.END+color.RED+' path in the project stack'+color.END)
                        __SHOW_STACK(showindexflag=False)

        else:
            print('project stack is '+color.RED+'empty.'+color.END+' do'+color.GREEN+' ```pwd | xargs pyramid --push``` '+color.END+'in you project directory.\n'+color.BLUE+'(or)'+color.GREEN+'\n--help | -h'+color.END+' for assistance.')




    elif sys.argv[1] == '--push':
        try:
            path = sys.argv[2]
            pathlist = []
            with open('/usr/local/bin/projectstack.csv','r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    pathlist.append(row['abs_path'])

            if(path not in pathlist):
                path = sys.argv[2]
                alias = path.split('/')[-1].strip()
                with open('/usr/local/bin/projectstack.csv','a') as f:
                    f.write(alias+','+path+',0')

                print('path added,do'+color.GREEN+' --show-stack to visualize'+color.END)
            else:
                print('path is already in the stack.')

        except IndexError:
            #italic command
            print('path is '+color.RED+'not provided'+color.END+', do'+color.GREEN+' pwd | xargs pyramid --push'+color.END+' in the directory you want to add.')


except KeyboardInterrupt:
    print(color.RED+'\nForce Quit!'+color.END)
