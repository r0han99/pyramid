#!/bin/bash

if [[ -f pyramid ]] && [[ -f pyramid-help.py ]] && [[ -f pyramidpy.py ]]
then    

    echo "Initiating install sequence"
    echo "You need root access for this procedure.Please enter your password correctly if prompted."
    sudo echo "This a temp file created while entering sudo mode" > .testrootfile.txt
    echo "Installing dependencies .. "
    echo ""
    sudo apt update && apt upgrade
    sudo apt install python3-pip
    sudo apt install tree
    sudo apt install xdg-open
    pip3 install pandas
    echo ""
    echo "Dependencies, Installed."
    echo ""
    echo "Adding Scripts to the PATH"
    sudo mv pyramid-help.py pyramid pyramidpy.py /usr/local/bin/
    echo ""
    echo "Scripts added. Now *-pyramid-* is a command-line utility."
    echo ""
    echo "Exec. Pyramid to setup project-stack."
    echo ""
    pyramid
    sudo rm .testrootfile.txt

else
    if [ -f /usr/local/bin/pyramid ]
    then
        echo "Pyramid-utility is already installed."
    else
        echo "Error [Incomplete requirements], reclone the repo if required."

    fi
fi

